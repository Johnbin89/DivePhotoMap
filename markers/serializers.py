from markers.models import Marker, DiveSpot
from rest_framework import serializers

class PublicDiveSpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiveSpot
        fields = ['name', 'description', 'accurate_location', 'dive_type', 'access_type']


class MarkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marker
        fields = ['url', 'posLat', 'posLng']

class PublicMarkerSerializer(serializers.HyperlinkedModelSerializer):
    divespot = PublicDiveSpotSerializer(many=False, read_only=True)
    class Meta:
        model = Marker
        fields = ['posLat', 'posLng', 'divespot']

class PublicDiveSpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marker
        fields = ['posLat', 'posLng']