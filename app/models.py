from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Grup adını ve isteğe bağlı olarak izinleri belirtin
group_name = "user_history"
group, created = Group.objects.get_or_create(name=group_name)
if created:
    print(f"Grup '{group_name}' başarıyla oluşturuldu.")

# Grup adını ve isteğe bağlı olarak izinleri belirtin
group_name = "user_operations"
group, created = Group.objects.get_or_create(name=group_name)
if created:
    print(f"Grup '{group_name}' başarıyla oluşturuldu.")

group_name = "parcel_edits"
group, created = Group.objects.get_or_create(name=group_name)
if created:
    print(f"Grup '{group_name}' başarıyla oluşturuldu.")

group_name = "analysis"
group, created = Group.objects.get_or_create(name=group_name)
if created:
    print(f"Grup '{group_name}' başarıyla oluşturuldu.")






class Parcel(models.Model):
    il = models.CharField(max_length=255)
    ilce = models.CharField(max_length=255)
    mevki = models.CharField(max_length=255)
    ada = models.CharField(max_length=255)
    parsel = models.CharField(max_length=255)
    m2_net = models.CharField(max_length=255)
    fiyat = models.CharField(max_length=255)
    durum = models.CharField(max_length=255, default='uygun')  
    user_id = models.CharField(max_length=255, default="None")
    bekleme_suresi_baslangic = models.DateTimeField(null=True, blank=True)
    bekleme_suresi_bitisi = models.DateTimeField(null=True, blank=True)
    bekleten_kullanici = models.CharField(max_length=255, default='None')


    def __str__(self):
        return self.parsel



class ParcelUserHistory(models.Model):
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User modeli ile ForeignKey ilişkisi
    tarih = models.DateField(auto_now_add=True)  # Tarih olarak saklamak için "DateField" kullanın
    saat = models.TimeField(auto_now_add=True)   # Saat olarak saklamak için "TimeField" kullanın
    islem = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.parcel} - {self.user_id} - Tarih: {self.tarih.strftime('%Y-%m-%d')}, Saat: {self.saat.strftime('%H:%M:%S')}"



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




class ParcelPricing(models.Model):

    il = models.CharField(max_length=255)
    ilce = models.CharField(max_length=255)
    mevki = models.CharField(max_length=255)
    fiyat = models.CharField(max_length=255, default="1")

    