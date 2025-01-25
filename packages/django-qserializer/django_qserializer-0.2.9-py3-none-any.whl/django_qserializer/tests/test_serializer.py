from unittest.mock import Mock

import pytest

from django_qserializer import BaseSerializer
from django_qserializer.tests.testapp.models import Bus, Company, Travel


@pytest.fixture
def bus_fixture(db):
    company = Company.objects.create(name='Hurricane Cart')
    return Bus.objects.create(company=company, plate='BUSER')


@pytest.fixture
def travel_fixture(db, bus_fixture):
    return Travel.objects.create(bus=bus_fixture)


def test_magic_serialize_method(bus_fixture, django_assert_num_queries):
    class S(BaseSerializer):
        select_related = ['company']

        def serialize_object(self, bus):
            return {
                'company': bus.company.name,
            }

    bus = Bus.objects.to_serialize(S).first()
    with django_assert_num_queries(0):
        assert {'company': 'Hurricane Cart'} == bus.serialize()


def test_serialize_object_not_implemented(bus_fixture):
    bus = Bus.objects.to_serialize().first()
    with pytest.raises(NotImplementedError):
        bus.serialize()


def test_extras(bus_fixture, django_assert_num_queries):
    class Attr(BaseSerializer):
        select_related = ['company']

        def serialize_object(self, obj):
            return {
                'myattr': obj.company.name
            }

    def func(obj):
        return {
            'seats': 32,
        }

    class S(BaseSerializer):
        extra = {
            'myattr': Attr,
            'func': func,
        }

        def serialize_object(self, obj):
            return {
                'plate': obj.plate,
            }

    serializer = S(extra=['myattr', 'func'])

    with django_assert_num_queries(1):
        bus = Bus.objects.to_serialize(serializer).first()

    expected = {
        'plate': 'BUSER',
        'myattr': 'Hurricane Cart',
        'seats': 32,
    }

    with django_assert_num_queries(0):
        assert expected == bus.serialize()


def test_extras_recursive(bus_fixture, django_assert_num_queries):
    def city(obj):
        return {
            'city': 'SJK',
        }

    class Attr(BaseSerializer):
        extra = {
            'city': city,
        }
        select_related = ['company']

        def serialize_object(self, obj):
            return {
                'myattr': obj.company.name
            }

    class S(BaseSerializer):
        extra = {
            'myattr': Attr(extra=['city']),
        }

        def serialize_object(self, obj):
            return {
                'plate': obj.plate,
            }

    serializer = S(extra=['myattr'])

    with django_assert_num_queries(1):
        bus = Bus.objects.to_serialize(serializer).first()

    expected = {
        'plate': 'BUSER',
        'myattr': 'Hurricane Cart',
        'city': 'SJK',
    }

    with django_assert_num_queries(0):
        assert expected == bus.serialize()


def test_extra_string_arg(bus_fixture, django_assert_num_queries):
    class S(BaseSerializer):
        extra = {
            'city': lambda obj: {'city': 'SJK'},
        }

        def serialize_object(self, obj):
            return {
                'plate': obj.plate,
            }

    serializer = S(extra='city')

    with django_assert_num_queries(1):
        bus = Bus.objects.to_serialize(serializer).first()

    expected = {
        'plate': 'BUSER',
        'city': 'SJK',
    }

    with django_assert_num_queries(0):
        assert expected == bus.serialize()


def test_prepare_objects_after_prefetch(travel_fixture):
    """
    Regression test. Prior implementation ran prepare_objects before prefetchs.
    """

    class S(BaseSerializer):
        prefetch_related = ['travels']

        def prepare_objects(self, objs):
            for obj in objs:
                assert obj._prefetched_objects_cache['travels']

        def serialize_object(self, obj):
            return {
                'plate': obj.plate,
            }

    bus = Bus.objects.to_serialize(S).first()
    bus.serialize()


def test_query_without_serializer(bus_fixture):
    """
    Regression test. Query without serializer failed.
    """
    Bus.objects.first()
    list(Bus.objects.all())


def test_values(bus_fixture):
    """
    Regression test.
    """
    qs = Bus.objects \
        .to_serialize(BaseSerializer) \
        .values('plate')
    plate = list(qs)[0]
    assert {'plate': 'BUSER'} == plate


def test_empty_result(db):
    Bus.objects.to_serialize(BaseSerializer).first()


def test_fetch_all_idempotent(bus_fixture):
    """
    Regression test. `QuerySet._fetch_all` is called a lot of times and Django
    execute queries once.
    """
    class S(BaseSerializer):
        prepare_objects = Mock()

    buses = Bus.objects.to_serialize(S).all()

    list(buses)
    S.prepare_objects.assert_called_once()

    list(buses)
    # The `prepare_objects` method was not called again.
    S.prepare_objects.assert_called_once()
