from .factories import UserFactory, VehicleFactory
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class BaseTestCase(APITestCase):
    @property
    def bearer_token(self):
        
        refresh = RefreshToken.for_user(self.user1_saved)
        return {"HTTP_AUTHORIZATION":f'Bearer {refresh.access_token}'}

    @property
    def invalid_bearer_token(self):

        invalid_token = 'this.is.invalid'
        return {"HTTP_AUTHORIZATION":f'Bearer {invalid_token}'}


    def setUp(self):
        self.user1_saved = UserFactory.create()
        self.user2_saved = UserFactory.create()
        self.vehicle1_saved = VehicleFactory.create(user=self.user1_saved)
        self.vehicle2_saved = VehicleFactory.create(user=self.user2_saved)
        self.client = APIClient()
