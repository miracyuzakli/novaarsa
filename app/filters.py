import django_filters
from .models import Parcel, ParcelUserHistory, SatisTakipModel

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



class ParcelUserHistoryFilter(django_filters.FilterSet):
    class Meta:
        model = ParcelUserHistory
        fields = {
            'parcel__il': ['exact', 'contains'],
            'parcel__ilce': ['exact', 'contains'],
            'parcel__mevki': ['exact', 'contains'],
            'parcel__ada': ['exact', 'contains'],
            'parcel__parsel': ['exact', 'contains'],
            'parcel__m2_net': ['exact', 'lt', 'lte', 'gt', 'gte'],
            'parcel__durum': ['exact', 'contains'],
            'user_id': ['exact', 'contains'],
            'tarih': ['exact', 'lt', 'lte', 'gt', 'gte'],
            'islem': ['exact', 'contains'],
        }



import django_filters

class SatisTakipModelFilter(django_filters.FilterSet):
    class Meta:
        model = SatisTakipModel
        fields = {
            'user_id': ['exact'],
            'parcel__il': ['exact', 'contains'],
            'parcel__ilce': ['exact', 'contains'],
            'parcel__mevki': ['exact', 'contains'],
            'parcel__ada': ['exact', 'contains'],
            'parcel__parsel': ['exact', 'contains'],
            'project_name': ['exact', 'contains'],
            'satis_danismani': ['exact', 'contains'],
            'satis_tarihi': ['exact', 'lt', 'lte', 'gt', 'gte'],
            'referans': ['exact', 'contains'],
            'ada': ['exact', 'contains'],
            'parcel_no': ['exact', 'contains'],
            'm2_bilgisi': ['exact', 'contains'],
            'hisse_adedi': ['exact', 'contains'],
            'firma_ad_soyad': ['exact', 'contains'],
            'TC_vergi_no': ['exact', 'contains'],
            'adres1': ['exact', 'contains'],
            'adres2': ['exact', 'contains'],
            'eposta': ['exact', 'contains'],
            'telefon_no': ['exact', 'contains'],
            'meslek_bilgisi': ['exact', 'contains'],
            'ulasamadigi_durumda_aranacak_kisi': ['exact', 'contains'],
            'ulasamadigi_durumda_aranacak_kisi_telefon_no': ['exact', 'contains'],
            'satis_fiyati': ['exact', 'contains'],
            'odeme_turu': ['exact', 'contains'],
            'on_odeme_tutari': ['exact', 'contains'],
            'odeme_tarihi': ['exact', 'lt', 'lte', 'gt', 'gte'],
            'pesinat_tutari': ['exact', 'contains'],
            'pesinat_tarihi': ['exact', 'lt', 'lte', 'gt', 'gte'],
            'm2_birim_fiyati': ['exact', 'contains'],
            'aciklama_bigisi': ['exact', 'contains'],
            'ek_bilgiler': ['exact', 'contains'],
        }
