import asyncio
from django.core.management.base import BaseCommand
from django.utils import timezone
from app.models import Parcel
from datetime import timedelta


class Command(BaseCommand):
    help = 'Bekleme süresi bitmiş parsel kayıtlarını tara'

    def handle(self, *args, **options):
        current_time = timezone.now() +  timedelta(minutes=180)
        expired_parcels = Parcel.objects.filter(bekleme_suresi_bitisi__lte=current_time)

        for parcel in expired_parcels:
            parcel.durum = 'uygun'
            parcel.bekleme_suresi_baslangic = None  # Null yapma
            parcel.bekleme_suresi_bitisi = None  # Null yapma
            parcel.bekleten_kullanici = "None"  # Null yapma
            parcel.user_id = "None"  # Null yapma
            
            
            parcel.save()
            self.stdout.write(self.style.SUCCESS(f'Süresi biten parsel (id={parcel.id}) güncellendi: süre bitti'))