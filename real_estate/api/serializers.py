from rest_framework import serializers

from contacts.models import Contact
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


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    contact_date = serializers.ReadOnlyField()
    user_id = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['listing']
