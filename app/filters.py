import django_filters
from .models import Parcel
class ParcelFilter(django_filters.FilterSet):
    class Meta:
        model = Parcel
        fields = {
            'parcel_no': ['exact', 'contains'],
            'parcel_name': ['exact', 'contains'],
            'm2': ['exact', 'lt', 'lte', 'gt', 'gte'],
            'status': ['exact', 'contains'],
        }
