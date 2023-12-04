from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Parcel  # .models, modelin bulunduğu dosyanın adıdır


class ParcelAdmin(admin.ModelAdmin):
    list_display = ('il', 'ilce', 'mevki', 'ada', 'parsel', 'm2_net', 'fiyat', 'durum', 'user_id')
    list_filter = ('il', 'ilce', 'durum')
    search_fields = ('ada', 'parsel', 'user_id')

admin.site.register(Parcel, ParcelAdmin)

# admin.site.register(Parcel)
