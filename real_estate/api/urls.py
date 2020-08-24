from django.urls import include, path
from rest_framework import routers

from . import views

# for Root api view
router = routers.DefaultRouter()
router.register(r'realtors', views.RealtorsViewSet)
router.register(r'listings', views.ListingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # to have log in option
]
