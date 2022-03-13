from factory import lazy_attribute, SubFactory, Iterator
from factory.django import DjangoModelFactory
from base.models import Vehicle
from .faker import faker
from .user_factory import UserFactory


VEHICLE_TYPE_KEYS = [x[0] for x in Vehicle.VEHICLE_TYPE_CHOICES]

class VehicleFactory(DjangoModelFactory):

    user = SubFactory(UserFactory)
    price = lazy_attribute(lambda x: faker.pydecimal(left_digits=13, right_digits=2, positive=True))
    vehicle_type = Iterator(VEHICLE_TYPE_KEYS)

    class Meta:
        model = Vehicle
