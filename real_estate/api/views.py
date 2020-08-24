from rest_framework import permissions
from rest_framework import viewsets

from listings.models import Listing
from realtors.models import Realtor
from .serializers import ListingSerializer, RealtorSerializer


class RealtorsViewSet(viewsets.ModelViewSet):
    """
    API endpoint to GET published realtors.
    """
    queryset = Realtor.objects.filter(is_published=True).order_by("-is_mvp", "hire_date")
    serializer_class = RealtorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint to GET published Listings.
    """
    queryset = Listing.objects.filter(is_published=True).order_by('-list_date')
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
