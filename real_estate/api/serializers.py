from secrets import compare_digest

from django.contrib.auth.models import User
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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)  # hide password2 field

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}  # hide password field
        }

    def save(self):  # override to compare passwords
        user = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if not compare_digest(password, password2):  # safer than != comparison
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        user.set_password(password)
        user.save()
        return user
