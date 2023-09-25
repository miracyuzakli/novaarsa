from django.db import models

# Create your models here.
class Parcel(models.Model):
    parcel_no = models.CharField(max_length=50)  # parcel_no için bir karakter alanı
    parcel_name = models.CharField(max_length=100)  # parcel_name için bir karakter alanı
    m2 = models.DecimalField(max_digits=10, decimal_places=2)  # m2 için ondalık sayı alanı (10 basamaklı, 2 ondalık basamak)
    status = models.CharField(max_length=20)  # status için bir karakter alanı

    def __str__(self):
        return self.parcel_name


class SatisTakip(models.Model):
    project_name = models.CharField(max_length=255)
    satis_danismani = models.CharField(max_length=255)
    satis_tarihi = models.DateField()
    referans = models.CharField(max_length=255)
    ada = models.CharField(max_length=255)
    parcel = models.CharField(max_length=255)
    m2_bilgisi = models.CharField(max_length=255)
    hisse_adedi = models.CharField(max_length=255)
    firma_ad_soyad = models.CharField(max_length=255)
    TC_vergi_no = models.CharField(max_length=255)
    adres1 = models.TextField()
    adres2 = models.TextField()
    eposta = models.EmailField()
    telefon_no = models.CharField(max_length=20)
    meslek_bilgisi = models.CharField(max_length=255)
    ulasamadigi_durumda_aranacak_kisi = models.CharField(max_length=255)
    ulasamadigi_durumda_aranacak_kisi_telefon_no = models.CharField(max_length=20)
    satis_fiyati = models.DecimalField(max_digits=10, decimal_places=2)
    on_odeme_tutari = models.DecimalField(max_digits=10, decimal_places=2)
    # odeme_tarihi = models.DateField()
    # pesinat_tutari = models.DecimalField(max_digits=10, decimal_places=2)
    # pesinat_tarihi = models.DateField()
    odeme_turu = models.CharField(max_length=255)
    m2_birim_fiyati = models.DecimalField(max_digits=10, decimal_places=2)
    aciklama_bigisi = models.TextField()
    ek_bilgiler = models.CharField(max_length=255)

    def __str__(self):
        return self.project_name  # Modelin hangi alanının metin temsili olacağını belirtiyoruz
