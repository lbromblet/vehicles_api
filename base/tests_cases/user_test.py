from django.urls import reverse
from rest_framework import status
from base.serializers import UserSerializer
from django.contrib.auth.models import User
from base.models import Vehicle
from .factories import UserFactory
from .base_test import BaseTestCase


class UserTestCase(BaseTestCase):

    def test_get_valid_single_user(self):
        """ GET single user OK."""
        response = self.client.get(reverse('user-detail', kwargs = {'pk' : self.user1_saved.pk}))
        user = User.objects.get(pk=self.user1_saved.pk)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """ POST user CREATED."""
        new_user = UserFactory.build()
        serializer = UserSerializer(new_user)
        request_data = serializer.data
        request_data['password'] = new_user.password
        request_data['password2'] = new_user.password
        response = self.client.post(reverse('user-list'), request_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_delete_no_bearer_user(self):
        """ DELETE user without authorization is UNAUTHORIZED."""
        response = self.client.delete(reverse('user-detail',
                                   kwargs = {'pk' : self.user1_saved.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_bearer_forbiden_user(self):
        """ DELETE user with authorization from other user is FORBIDDEN."""
        response = self.client.delete(reverse('user-detail',
                                   kwargs = {'pk' : self.user2_saved.pk}),
                                   **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_bearer_valid_user(self):
        """ 
        DELETE user with authorization from user being deleted.
        Check if user's vehicles are deleted after his own deletion.
        """
        vehicles = Vehicle.objects.all()
        vehicles_count = vehicles.count()
        vehicles_user1 = Vehicle.objects.filter(user = self.user1_saved)
        vehicles_user1_count = vehicles_user1.count()
        response = self.client.delete(reverse('user-detail',
                                   kwargs = {'pk' : self.user1_saved.pk}),
                                   **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        vehicles = Vehicle.objects.all()
        updated_vehicles_count = vehicles.count()
        self.assertEqual(updated_vehicles_count, (vehicles_count-vehicles_user1_count))
