from django.db import models

# Create your models here.
class Marker(models.Model):
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    public = models.BooleanField()
    posLat = models.DecimalField(verbose_name='Marker Latitude', max_digits=7, decimal_places=5)
    posLng = models.DecimalField(verbose_name='Marker Longitude', max_digits=7, decimal_places=5)
    divespot = models.OneToOneField('DiveSpot', related_name='marker_divespot', on_delete=models.CASCADE)

class DiveSpot(models.Model):
    name = models.CharField(max_length=50, verbose_name="divespot_name")
    description = models.TextField(blank=True, verbose_name="divespot_description")
    accurate_location = models.BooleanField()
    dive_type__choices = [
        ('Reef', 'Reef'),
        ('Wall', 'Wall'),
        ('Wreck', 'Wreck'),
        ('Cave', 'Cave'),
        ('Cavern', 'Cavern'),
        ('Open Water', 'Open Water'),
    ]
    dive_type = models.CharField(max_length=30, choices=dive_type__choices, default='Open Water')
    access_type__choices = [
        ('On Foot', 'On Foot'),
        ('By Boat', 'By Boat'),
        ('Unknown', 'Unknown'),
    ]
    access_type = models.CharField(max_length=30, choices=access_type__choices, default='Unknown')    