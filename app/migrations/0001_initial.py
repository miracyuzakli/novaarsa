# Generated by Django 4.2.5 on 2024-01-09 03:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('il', models.CharField(max_length=255)),
                ('ilce', models.CharField(max_length=255)),
                ('mevki', models.CharField(max_length=255)),
                ('ada', models.CharField(max_length=255)),
                ('parsel', models.CharField(max_length=255)),
                ('m2_net', models.CharField(max_length=255)),
                ('fiyat', models.CharField(max_length=255)),
                ('durum', models.CharField(max_length=255)),
                ('menu_name', models.CharField(max_length=255)),
                ('user_id', models.CharField(default='None', max_length=255)),
                ('bekleme_suresi_baslangic', models.DateTimeField(blank=True, null=True)),
                ('bekleme_suresi_bitisi', models.DateTimeField(blank=True, null=True)),
                ('bekleten_kullanici', models.CharField(default='None', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ParcelPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('il', models.CharField(max_length=255)),
                ('ilce', models.CharField(max_length=255)),
                ('mevki', models.CharField(max_length=255)),
                ('fiyat', models.CharField(default='1', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SatisTakipModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='None', max_length=255)),
                ('project_name', models.CharField(max_length=255)),
                ('satis_danismani', models.CharField(max_length=255)),
                ('satis_tarihi', models.DateField()),
                ('referans', models.CharField(max_length=255)),
                ('ada', models.CharField(max_length=255)),
                ('parcel_no', models.CharField(max_length=255)),
                ('m2_bilgisi', models.CharField(max_length=255)),
                ('hisse_adedi', models.CharField(max_length=255)),
                ('firma_ad_soyad', models.CharField(max_length=255)),
                ('TC_vergi_no', models.CharField(max_length=255)),
                ('adres1', models.TextField()),
                ('adres2', models.TextField()),
                ('eposta', models.EmailField(max_length=254)),
                ('telefon_no', models.CharField(max_length=20)),
                ('meslek_bilgisi', models.CharField(max_length=255)),
                ('ulasamadigi_durumda_aranacak_kisi', models.CharField(max_length=255)),
                ('ulasamadigi_durumda_aranacak_kisi_telefon_no', models.CharField(max_length=20)),
                ('satis_fiyati', models.CharField(max_length=255)),
                ('odeme_turu', models.CharField(max_length=255)),
                ('on_odeme_tutari', models.CharField(max_length=255)),
                ('odeme_tarihi', models.DateField(blank=True, null=True)),
                ('pesinat_tutari', models.CharField(max_length=255)),
                ('pesinat_tarihi', models.DateField(blank=True, null=True)),
                ('m2_birim_fiyati', models.CharField(max_length=255)),
                ('aciklama_bigisi', models.TextField()),
                ('ek_bilgiler', models.CharField(max_length=255)),
                ('kampanya_kodu', models.CharField(max_length=255)),
                ('musteri_iban', models.CharField(max_length=255)),
                ('parcel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.parcel')),
            ],
        ),
        migrations.CreateModel(
            name='ParcelWaiting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcel_waiting', models.IntegerField(default=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParcelUserHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarih', models.DateField(auto_now_add=True)),
                ('saat', models.TimeField(auto_now_add=True)),
                ('islem', models.CharField(max_length=255)),
                ('parcel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.parcel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
