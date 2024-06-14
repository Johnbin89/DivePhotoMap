from django.shortcuts import render
from rest_framework import generics, permissions, status
from markers.models import Marker
from markers.serializers import MarkerSerializer
from markers.permissions import IsOwner
# Create your views here.


class PublicMarkerList(generics.ListAPIView):
    queryset = Marker.objects.filter(public=True)
    serializer_class = MarkerSerializer


class UserMarkers(generics.ListCreateAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
    permission_classes=[IsOwner]


class UserMarkersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
    permission_classes=[IsOwner]