from django.contrib import admin
from .models import Parcel, ParcelUserHistory, SatisTakipModel, ParcelPricing, ParcelWaiting


# class ParcelAdmin(admin.ModelAdmin):
#     list_display = ('il', 'ilce', 'mevki', 'ada', 'parsel', 'm2_net', 'fiyat', 'durum', 'user_id')
#     list_filter = ('il', 'ilce', 'durum')
#     search_fields = ('ada', 'parsel', 'user_id')

# admin.site.register(Parcel, ParcelAdmin)

# admin.site.register(Parcel)


class ParcelAdmin(admin.ModelAdmin):
    list_display = ['il', 'ilce', 'mevki', 'ada', 'parsel', 'm2_net', 'fiyat', 'durum', 'user_id', 'bekleme_suresi_baslangic', 'bekleme_suresi_bitisi', 'bekleten_kullanici']

admin.site.register(Parcel, ParcelAdmin)

class ParcelUserHistoryAdmin(admin.ModelAdmin):
    list_display = ['parcel', 'user', 'tarih', 'saat', 'islem']

admin.site.register(ParcelUserHistory, ParcelUserHistoryAdmin)

class SatisTakipModelAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'parcel', 'project_name', 'satis_danismani', 'satis_tarihi', 'referans', 'ada', 'parcel_no', 'm2_bilgisi', 'hisse_adedi', 'firma_ad_soyad', 'TC_vergi_no', 'adres1', 'adres2', 'eposta', 'telefon_no', 'meslek_bilgisi', 'ulasamadigi_durumda_aranacak_kisi', 'ulasamadigi_durumda_aranacak_kisi_telefon_no', 'satis_fiyati', 'odeme_turu', 'on_odeme_tutari', 'odeme_tarihi', 'pesinat_tutari', 'pesinat_tarihi', 'm2_birim_fiyati', 'aciklama_bigisi', 'ek_bilgiler']

admin.site.register(SatisTakipModel, SatisTakipModelAdmin)

class ParcelPricingAdmin(admin.ModelAdmin):
    list_display = ['il', 'ilce', 'mevki', 'fiyat']

admin.site.register(ParcelPricing, ParcelPricingAdmin)

class ParcelWaitingAdmin(admin.ModelAdmin):
    list_display = ['user', 'parcel_waiting']

admin.site.register(ParcelWaiting, ParcelWaitingAdmin)
