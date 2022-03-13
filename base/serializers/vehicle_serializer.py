from base.models import Vehicle
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, 
        default=serializers.CurrentUserDefault()
    )
    vehicle_type = serializers.ChoiceField(choices=Vehicle.VEHICLE_TYPE_CHOICES)
    user_username = serializers.CharField(read_only=True, source='user.username')

    class Meta:
        model = Vehicle
        fields = ['id', 'vehicle_type', 'user', 'price', 'created', 'updated', 'user_username']
