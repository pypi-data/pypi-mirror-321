import types

from django.db import models
from django.db.models.manager import BaseManager


class _SerializationWrapper:
    """Method wrapper to make a picklable object."""

    def __init__(self, serializer, obj):
        self.serializer = serializer
        self.obj = obj

    def __call__(self):
        return self.serializer._serialize_object(self.obj)


class BaseSerializer:
    select_related = None
    prefetch_related = None
    extra = None

    def __init__(self, *, select_related=None, prefetch_related=None, extra=None):
        if select_related:
            self.select_related = select_related
        if prefetch_related:
            self.prefetch_related = prefetch_related

        if extra:
            if isinstance(extra, str):
                extra = [extra]
            self.extra = {key: _resolve_serializer(self.extra[key]) for key in extra}
        else:
            self.extra = {}

    def _prepare_queryset(self, qs):
        if self.select_related:
            if callable(self.select_related):
                qs = qs.select_related(*self.select_related())
            else:
                qs = qs.select_related(*self.select_related)

        if self.prefetch_related:
            if callable(self.prefetch_related):
                qs = qs.prefetch_related(*self.prefetch_related())
            else:
                qs = qs.prefetch_related(*self.prefetch_related)

        qs = self.prepare_queryset(qs)

        for extra in self.extra.values():
            qs = extra._prepare_queryset(qs)

        return qs

    def prepare_queryset(self, qs):
        """
        Custom change the queryset. It is possible to implement `select_related`
        and `prefetch_related` attributes with it, but they work nice together.
        """
        return qs

    def _prepare_objects(self, objs):
        self.prepare_objects(objs)

        for extra in self.extra.values():
            extra._prepare_objects(objs)

        for obj in objs:
            obj.serialize = _SerializationWrapper(self, obj)

    def prepare_objects(self, objs):
        """
        Prepare objects after they are loaded to memory.

        It is a hook to add data in bulk to loaded objects, like fetching info
        from cache and attaching to them.
        """
        pass

    def _serialize_object(self, obj):
        serialized = self.serialize_object(obj)
        for extra in self.extra.values():
            serialized.update(extra._serialize_object(obj))
        return serialized

    def serialize_object(self, obj):
        """
        Required implementation. It converts the Django model to a serializable
        dict.

        Avoid slow calls here because it will cause N+1 issues.
        """
        raise NotImplementedError


class SerializableQuerySet(models.QuerySet):
    @property
    def serializer(self):
        return getattr(self, '_serializer', None)

    def to_serialize(self, serializer=None):
        self._serializer = _resolve_serializer(serializer)
        return self._serializer._prepare_queryset(self)

    def _fetch_all(self):
        result_already_cached = self._result_cache is not None
        super()._fetch_all()
        if result_already_cached or not self._result_cache:
            return

        serializer = self.serializer

        if serializer and isinstance(self._result_cache[0], models.Model):
            serializer._prepare_objects(self._result_cache)

    def _clone(self):
        c = super()._clone()
        c._serializer = self.serializer
        return c


class SerializableManager(BaseManager.from_queryset(SerializableQuerySet)):
    def __init__(self, *, select_related=None, prefetch_related=None,
                 default_serializer=BaseSerializer):
        super().__init__()
        self.default_serializer = default_serializer(
            select_related=select_related,
            prefetch_related=prefetch_related,
        )

    def to_serialize(self, serializer=None):
        if serializer is None:
            serializer = self.default_serializer
        return self.get_queryset().to_serialize(serializer)

    @classmethod
    def from_queryset(cls, queryset_class, class_name=None):
        if not hasattr(queryset_class, 'to_serialize'):
            queryset_class = type(
                f'SerializableQuerySet__{queryset_class.__name__}',
                (SerializableQuerySet, queryset_class), {})
        return super().from_queryset(queryset_class, class_name=class_name)


class _FuncSerializer(BaseSerializer):
    def __init__(self, func):
        super().__init__()
        self.func = func

    def serialize_object(self, obj):
        return self.func(obj)


def _resolve_serializer(serializer):
    if isinstance(serializer, types.FunctionType):
        serializer = _FuncSerializer(serializer)
    elif not isinstance(serializer, BaseSerializer):
        serializer = serializer()
    return serializer
