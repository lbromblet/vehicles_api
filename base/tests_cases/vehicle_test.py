from django.urls import reverse
from rest_framework import status
from base.serializers import VehicleSerializer
from base.models import Vehicle
from .factories import VehicleFactory
from .base_test import BaseTestCase


class VehicleTestCase(BaseTestCase):

    def test_get_valid_single_vehicle(self):
        """ GET single vehicle OK."""
        response = self.client.get(reverse('vehicle-detail', kwargs = {'pk' : self.vehicle1_saved.pk}))
        vehicle = Vehicle.objects.get(pk=self.vehicle1_saved.pk)
        serializer = VehicleSerializer(vehicle)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_vehicle(self):
        """ GET single vehicle NOT_FOUND."""
        response = self.client.get(reverse('vehicle-detail', kwargs = {'pk' : 99}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_vehicle(self):
        """ GET vehicle list OK."""
        response = self.client.get(reverse('vehicle-list'))
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_no_bearer_vehicle(self):
        """ POST vehicle without authorization UNAUTHORIZED."""
        new_vehicle = VehicleFactory.build(user=self.user1_saved)
        serializer = VehicleSerializer(new_vehicle)
        request_data = serializer.data
        response = self.client.post(reverse('vehicle-list'), request_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_invalid_bearer_vehicle(self):
        """ POST vehicle with invalid authorization UNAUTHORIZED."""
        new_vehicle = VehicleFactory.build(user=self.user1_saved)
        serializer = VehicleSerializer(new_vehicle)
        request_data = serializer.data
        response = self.client.post(reverse('vehicle-list'), request_data, **self.invalid_bearer_token)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_bearer_valid_vehicle(self):
        """ POST vehicle with valid authorization CREATED."""
        new_vehicle = VehicleFactory.build(user=self.user1_saved)
        serializer = VehicleSerializer(new_vehicle)
        request_data = serializer.data
        response = self.client.post(reverse('vehicle-list'), request_data, **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_no_bearer_vehicle(self):
        """ PUT vehicle without authorization UNAUTHORIZED."""
        new_vehicle = VehicleFactory.build(user=self.user1_saved)
        serializer = VehicleSerializer(new_vehicle)
        request_data = serializer.data
        del request_data['user']
        response = self.client.put(reverse('vehicle-detail',
                                   kwargs = {'pk' : self.vehicle1_saved.pk}),
                                   request_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_forbiden_bearer_vehicle(self):
        """ PUT vehicle with authorization from other user than vehicle's owner FORBIDDEN."""
        new_vehicle = VehicleFactory.build()
        serializer = VehicleSerializer(new_vehicle)
        request_data = serializer.data
        del request_data['user']
        response = self.client.put(reverse('vehicle-detail',
                                   kwargs = {'pk' : self.vehicle2_saved.pk}),
                                   request_data,
                                   **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_bearer_valid_vehicle(self):
        """ PUT vehicle with valid authorization from vehicle's owner user OK."""
        new_vehicle = VehicleFactory.build(user=self.user1_saved)
        serializer = VehicleSerializer(new_vehicle)
        request_data = serializer.data
        del request_data['user']
        response = self.client.put(reverse('vehicle-detail',
                                   kwargs = {'pk' : self.vehicle1_saved.pk}),
                                   request_data,
                                   **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_no_bearer_vehicle(self):
        """ DELETE vehicle without authorization UNAUTHORIZED."""
        response = self.client.delete(reverse('vehicle-detail',
                                   kwargs = {'pk' : self.vehicle1_saved.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_bearer_forbiden_vehicle(self):
        """ DELETE vehicle with authorization from other user than vehicle's owner FORBIDDEN."""
        response = self.client.delete(reverse('vehicle-detail',
                                   kwargs = {'pk' : self.vehicle2_saved.pk}),
                                   **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_bearer_valid_vehicle(self):
        """ DELETE vehicle with valid authorization from vehicle's owner user OK."""
        response = self.client.delete(reverse('vehicle-detail',
                                   kwargs = {'pk' : self.vehicle1_saved.pk}),
                                   **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
