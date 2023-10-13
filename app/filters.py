import django_filters
from .models import Parcel, ParcelPricing, ParcelUserHistory, SatisTakipModel

class ParcelFilter(django_filters.FilterSet):
    class Meta:
        model = Parcel
        fields = {
            'il': ['exact', 'contains'],
            'ilce': ['exact', 'contains'],
            'mevki': ['exact', 'contains'],
            'ada': ['exact', 'contains'],
            'parsel': ['exact', 'contains'],
            'm2_net': ['exact', 'lt', 'lte', 'gt', 'gte'],
            'durum': ['exact', 'contains'],
            'user_id': ['exact', 'contains'],  # Add user_id filter
            'bekleme_suresi_baslangic': ['exact', 'lt', 'lte', 'gt', 'gte'],  # Add bekleme_suresi_baslangic filter
            'bekleme_suresi_bitisi': ['exact', 'lt', 'lte', 'gt', 'gte'],  # Add bekleme_suresi_bitisi filter
        }



import django_filters

class ParcelPricingFilter(django_filters.FilterSet):
    class Meta:
        model = ParcelPricing
        fields = ['il', 'ilce', 'mevki', 'fiyat']
