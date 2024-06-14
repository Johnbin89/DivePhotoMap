from django.db import models

# Create your models here.
class Marker(models.Model):
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    posLat = models.DecimalField(verbose_name='Marker Latitude')
    posLng = models.DecimalField(verbose_name='Marker Longitude')