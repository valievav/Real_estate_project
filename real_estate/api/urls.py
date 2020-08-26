from django.urls import include, path
from rest_framework import routers

from . import views

# Root API view
router = routers.DefaultRouter()
router.register(r'realtors', views.RealtorsViewSet, basename="realtor")
router.register(r'listings', views.ListingViewSet, basename="listing")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # to have log in option
]
