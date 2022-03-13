from base.models import Vehicle
from base.serializers import VehicleSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import rest_framework as filters_drf
from base.filters import VehicleFilter
from base.pagination import SmallResultsSetPagination


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the vehicle.
        return obj.user == request.user


class VehicleViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,\
                     UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    A viewset for viewing and editing vehicle instances.
    """

    queryset = Vehicle.objects.all()

    serializer_class = VehicleSerializer
    filterset_class = VehicleFilter
    pagination_class = SmallResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [OrderingFilter, SearchFilter, filters_drf.DjangoFilterBackend,]
    ordering_fields = ['created', 'price']
    ordering = ['created']
    search_fields = ['user__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
