from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

# Root API view
router = routers.DefaultRouter()
router.register(r'realtors', views.RealtorsViewSet, basename="realtor")
router.register(r'listings', views.ListingViewSet, basename="listing")
router.register(r'contact', views.ContactViewSet, basename="contact")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # to have log in option
    path('account/register/', views.registration_view, name='register'),
    path('token/', TokenObtainPairView.as_view()),  # get 2 tokens (assess and refresh) for registered user
    path('token/refresh/', TokenRefreshView.as_view()),  # to get new access token using refresh token from prev. call
]
