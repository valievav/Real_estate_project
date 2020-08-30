from django.db.models import Q
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from contacts.models import Contact
from listings.models import Listing
from realtors.models import Realtor
from .serializers import ListingSerializer, RealtorSerializer, ContactSerializer, UserSerializer


class RealtorsViewSet(viewsets.ModelViewSet):
    """
    API endpoint for realtors.
    """
    queryset = Realtor.objects.filter(is_published=True).order_by("-is_mvp", "hire_date")
    serializer_class = RealtorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listings.
    Can be filtered by 'keywords', 'city', 'state', 'bedrooms', 'price'.
    Example: api/listings/?bedrooms=5&price=400000
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


class ContactViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    API endpoint for contacts.
    """
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return Contact.objects.filter(user_id=user_id).order_by('-contact_date')

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)  # set user to the current user automatically


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered new user."
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['username'] = user.username
            data['email'] = user.email
        else:
            data = serializer.errors

        return Response(data)
