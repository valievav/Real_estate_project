from rest_framework import serializers
from listings.models import Listing
from realtors.models import Realtor


class RealtorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Realtor
        fields = '__all__'


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    realtor = serializers.StringRelatedField()  # to display realtor name that belongs to different model

    class Meta:
        model = Listing
        fields = '__all__'
