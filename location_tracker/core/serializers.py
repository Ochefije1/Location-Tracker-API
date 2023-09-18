from rest_framework import serializers
from .models import PhoneNumberLocation

class PhoneNumberLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumberLocation
        fields = '__all__'
