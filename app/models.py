from django.db import models
from django.contrib.auth.models import User

class Parcel(models.Model):
    il = models.CharField(max_length=255)
    ilce = models.CharField(max_length=255)
    mevki = models.CharField(max_length=255)
    ada = models.CharField(max_length=255)
    parsel = models.CharField(max_length=255)
    m2_net = models.DecimalField(max_digits=10, decimal_places=2)
    durum = models.CharField(max_length=255, default='uygun')  
    user_id = models.CharField(max_length=255, default="None")
    bekleme_suresi_baslangic = models.DateField(null=True, blank=True)
    bekleme_suresi_bitisi = models.DateField(null=True, blank=True)
    bekleten_kullanici = models.CharField(max_length=255, default='None')


    def __str__(self):
        return self.parsel

class ParcelUserHistory(models.Model):
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=255)  
    tarih = models.DateTimeField(auto_now_add=True)  
    islem = models.CharField(max_length=255) 

    def __str__(self):
        return f"{self.parcel} - {self.user_id} - {self.tarih}"


class SatisTakipModel(models.Model):

    user_id = models.CharField(max_length=255, default="None")  
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)

    project_name = models.CharField(max_length=255)
    satis_danismani = models.CharField(max_length=255)
    satis_tarihi = models.DateField()
    referans = models.CharField(max_length=255)
    ada = models.CharField(max_length=255)
    parcel_no = models.CharField(max_length=255)
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
    satis_fiyati = models.CharField(max_length=255)
    odeme_turu = models.CharField(max_length=255)
    on_odeme_tutari = models.CharField(max_length=255)
    odeme_tarihi = models.DateField(null=True, blank=True)
    pesinat_tutari = models.CharField(max_length=255)
    pesinat_tarihi = models.DateField(null=True, blank=True)
    m2_birim_fiyati = models.CharField(max_length=255)
    aciklama_bigisi = models.TextField()
    ek_bilgiler = models.CharField(max_length=255)

    def __str__(self):
        return (
            self.project_name
        ) 
