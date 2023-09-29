from rest_framework import serializers
from .models import Parcel, ParcelUserHistory, SatisTakipModel

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'


class ParcelUserHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelUserHistory
        fields = '__all__'


class SatisTakipModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SatisTakipModel
        fields = '__all__'