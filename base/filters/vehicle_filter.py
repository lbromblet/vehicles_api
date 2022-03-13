from django_filters.rest_framework import FilterSet, NumberFilter, ChoiceFilter
from base.models import Vehicle


class VehicleFilter(FilterSet):

    vehicle_type = ChoiceFilter(choices=Vehicle.VEHICLE_TYPE_CHOICES)
    price_gte = NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = NumberFilter(field_name='price', lookup_expr='lte')
    price_gt = NumberFilter(field_name='price', lookup_expr='gt')
    price_lt = NumberFilter(field_name='price', lookup_expr='lt')
    
    class Meta:
        model = Vehicle
        fields = ['vehicle_type', 'price_gte', 'price_lte', 'price_gt', 'price_lt']
