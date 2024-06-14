from django.db import models

# Create your models here.
class Marker(models.Model):
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    public = models.BooleanField()
    posLat = models.DecimalField(verbose_name='Marker Latitude', max_digits=7, decimal_places=5)
    posLng = models.DecimalField(verbose_name='Marker Longitude', max_digits=7, decimal_places=5)