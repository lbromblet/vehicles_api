from django.contrib.auth import get_user_model
from factory import LazyAttribute
from factory.django import DjangoModelFactory
from .faker import faker

User = get_user_model()

class UserFactory(DjangoModelFactory):

    class Meta:
        model = User
    
    first_name = LazyAttribute(lambda x: faker.first_name())
    last_name = LazyAttribute(lambda x: faker.last_name())
    username = LazyAttribute(lambda x: faker.email())
    email = LazyAttribute(lambda x: faker.email())
    password = LazyAttribute(lambda x: faker.password())

    @staticmethod
    def generate_password():
        return faker.password()
