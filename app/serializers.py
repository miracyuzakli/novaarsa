from rest_framework import serializers
from .models import Parcel, ParcelPricing, ParcelUserHistory, SatisTakipModel
from django.contrib.auth.models import User

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'


class ParcelPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelPricing
        fields = '__all__'  # Tüm alanları dahil etmek isterseniz


class SatisTakipModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SatisTakipModel
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
