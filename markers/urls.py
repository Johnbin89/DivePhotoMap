from django.urls import path, include
from markers import views





urlpatterns = [
    # URLs for class-based views (Generics, APIViews)
    path('public/', views.PublicMarkerList.as_view(), name='markers_public'),
    path('private/', views.UserMarkers.as_view(), name='markers_private'),
    path('private/<int:pk>', views.UserMarkersDetail.as_view(), name='marker_private')
]