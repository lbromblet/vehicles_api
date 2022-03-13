from django.contrib.admin import ModelAdmin, register
from base.models import Vehicle


@register(Vehicle)
class VehicleAdmin(ModelAdmin):
    list_display = ('vehicle_type', 'price', 'user',)
    ordering = ('price',)