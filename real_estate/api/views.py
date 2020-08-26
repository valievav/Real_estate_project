from django.db.models import Q
from rest_framework import permissions
from rest_framework import viewsets

from listings.models import Listing
from realtors.models import Realtor
from .serializers import ListingSerializer, RealtorSerializer


class RealtorsViewSet(viewsets.ModelViewSet):
    """
    API endpoint for realtors.
    Note: create/update/delete calls available only for authenticated users.
    """
    queryset = Realtor.objects.filter(is_published=True).order_by("-is_mvp", "hire_date")
    serializer_class = RealtorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listings.
    Can be filtered by 'keywords', 'city', 'state', 'bedrooms', 'price'  (e.g /api/listings/?bedrooms=5&price=400000).
    Note: create/update/delete calls available only for authenticated users.
    """
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # overwrite queryset with custom search
    def get_queryset(self):
        queryset = Listing.objects.filter(is_published=True).order_by('-list_date')

        keywords = self.request.query_params.get('keywords')
        city = self.request.query_params.get('city')
        state = self.request.query_params.get('state')
        bedrooms = self.request.query_params.get('bedrooms')
        price = self.request.query_params.get('price')

        if keywords:
            queryset = queryset.filter(Q(title__icontains=keywords) | Q(description__icontains=keywords))
        if city:
            queryset = queryset.filter(city__iexact=city)
        if state and state != 'All':
            queryset = queryset.filter(state__iexact=state)
        if bedrooms and bedrooms != 'Any':
            queryset = queryset.filter(bedrooms__lte=bedrooms)
        if price and price != 'Any':
            queryset = queryset.filter(price__lte=price)

        return queryset
