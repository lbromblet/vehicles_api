from django.db import models
from django.contrib.auth.models import User


class Vehicle(models.Model):
    """Defines vehicles data for existing ClimavistaPaises.

    * Description
    None

    * Additional data
    None


    * Attributes
    ** user: User owner of the vehicle
    ** vehicle_type: Type of vehicle
    ** price: Price of the vehicle
    ** updated: date of most recent update
    ** created: date of creation

    * Properties
    None
    
    * Methods
    None
    """

    VEHICLE_TYPE_CHOICES = (('car', 'Car'),
                            ('motorcycle', 'MotorCycle'),
                            ('van', 'Van'))
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    vehicle_type = models.CharField(choices=VEHICLE_TYPE_CHOICES, blank=False, null=False, max_length=10)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(dict(self.VEHICLE_TYPE_CHOICES)[self.vehicle_type], self.price)

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
        db_table = 'vehicles'
