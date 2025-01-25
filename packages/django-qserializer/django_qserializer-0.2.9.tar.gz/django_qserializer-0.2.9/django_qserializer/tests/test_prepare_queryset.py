from django.db import models
import pytest

from django_qserializer import BaseSerializer, SerializableManager, SerializableQuerySet
from django_qserializer.tests.testapp.models import Bus, Company


@pytest.fixture
def bus_fixture(db):
    company = Company.objects.create()
    return Bus.objects.create(company=company)


def test_manager_works(bus_fixture, db, django_assert_num_queries):
    class S(BaseSerializer):
        pass

    bus = Bus.objects.to_serialize(S).first()
    with django_assert_num_queries(1):
        bus.company


def test_select_related_attr(bus_fixture, db, django_assert_num_queries):
    class S(BaseSerializer):
        select_related = ['company']

    bus = Bus.objects.to_serialize(S).first()
    with django_assert_num_queries(0):
        bus.company


def test_prefetch_related_attr(bus_fixture, db, django_assert_num_queries):
    class S(BaseSerializer):
        prefetch_related = ['company']

    with django_assert_num_queries(2):
        # bus query + company prefetch query
        bus = Bus.objects.to_serialize(S).first()

    with django_assert_num_queries(0):
        bus.company


def test_select_related_callable(bus_fixture, db, django_assert_num_queries):
    class S(BaseSerializer):
        def select_related(self):
            return ['company']

    bus = Bus.objects.to_serialize(S).first()
    with django_assert_num_queries(0):
        bus.company


def test_prefetch_related_callable(bus_fixture, db, django_assert_num_queries):
    class S(BaseSerializer):
        def prefetch_related(self):
            return ['company']

    with django_assert_num_queries(2):
        # bus query + company prefetch query
        bus = Bus.objects.to_serialize(S).first()

    with django_assert_num_queries(0):
        bus.company


def test_default_serializer_select_related(bus_fixture, db, django_assert_num_queries):
    class BusProxySelectRelated(Bus):
        objects = SerializableManager(
            select_related=['company'],
        )

        class Meta:
            app_label = 'testapp'
            proxy = True

    bus = BusProxySelectRelated.objects.to_serialize().first()
    with django_assert_num_queries(0):
        bus.company


def test_default_serializer_prefetch_related(bus_fixture, db, django_assert_num_queries):
    class BusProxyPrefetchRelated(Bus):
        objects = SerializableManager(
            prefetch_related=['company'],
        )

        class Meta:
            app_label = 'testapp'
            proxy = True

    with django_assert_num_queries(2):
        bus = BusProxyPrefetchRelated.objects.to_serialize().first()

    with django_assert_num_queries(0):
        bus.company


def test_from_queryset_with_serializable_queryset(bus_fixture):
    class CustomQuerySet(SerializableQuerySet):
        pass

    class BusProxySerializableQuerySet(Bus):
        objects = SerializableManager.from_queryset(CustomQuerySet)()

        class Meta:
            app_label = 'testapp'
            proxy = True

    BusProxySerializableQuerySet.objects.to_serialize().first()


def test_from_queryset_with_custom_queryset(bus_fixture):
    class CustomQuerySet(models.QuerySet):
        pass

    class BusProxyCustomQuerySet(Bus):
        objects = SerializableManager.from_queryset(CustomQuerySet)()

        class Meta:
            app_label = 'testapp'
            proxy = True

    BusProxyCustomQuerySet.objects.to_serialize().first()
