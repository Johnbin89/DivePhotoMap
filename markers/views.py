from django.shortcuts import render
from rest_framework import generics, permissions, status
from markers.models import Marker
from markers.serializers import MarkerSerializer, PublicMarkerSerializer
from markers.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class PublicMarkerList(generics.ListAPIView):
    queryset = Marker.objects.filter(public=True)
    serializer_class = PublicMarkerSerializer
    permission_classes=[permissions.AllowAny]


class UserMarkers(generics.ListCreateAPIView):
    serializer_class = MarkerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Marker.objects.filter(owner=user)


class UserMarkersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
    authentication_classes = [JWTAuthentication]
    #IsOwner permission works for single objects.
    permission_classes=[IsOwner, IsAuthenticated]
