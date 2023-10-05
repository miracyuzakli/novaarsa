
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from ..models import Parcel, SatisTakipModel, ParcelUserHistory
from ..serializers import ParcelSerializer, SatisTakipModelSerializer
from ..filters import ParcelFilter, SatisTakipModelFilter

from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils import timezone  # Django'nun zaman dilimi işlevlerini içe aktarın
from datetime import datetime, timedelta




#! Applications
class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ParcelFilter



class SatisTakipModelViewSet(viewsets.ModelViewSet):
    queryset = SatisTakipModel.objects.all()
    serializer_class = SatisTakipModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SatisTakipModelFilter




@csrf_protect
def save_form_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

           

            if data["banka_odeme"] == True:
                odeme_yontemi = "banka"
            elif data["vadeli_odeme"] == True:
                odeme_yontemi = "vadeli"
            elif data["pesin_odeme"] == True:  
                odeme_yontemi = "pesin"

            # parcel = Parcel(pk=data["parsel_id"])
            parcel = Parcel.objects.get(pk=data["parsel_id"])  # Örnek olarak bir parcel nesnesi alın

           

            # Verileri SatisTakip modeline kaydet
            satis_takip = SatisTakipModel(
            user_id=request.user.id,
            parcel=parcel,
            project_name=data['project_name'],
            satis_danismani=data['satis_danismani'],
            satis_tarihi=data['satis_tarihi'],
            referans=data['referans'],
            ada=data['ada'],
            parcel_no=data['parcel_no'],
            m2_bilgisi=data['m2_bilgisi'],
            hisse_adedi=data['hisse_adedi'],
            firma_ad_soyad=data['firma_ad_soyad'],
            TC_vergi_no=data['TC_vergi_no'],
            adres1=data['adres1'],
            adres2=data['adres2'],
            eposta=data['eposta'],
            telefon_no=data['telefon_no'],
            meslek_bilgisi=data['meslek_bilgisi'],
            ulasamadigi_durumda_aranacak_kisi=data['ulasamadigi_durumda_aranacak_kisi'],
            ulasamadigi_durumda_aranacak_kisi_telefon_no=data['ulasamadigi_durumda_aranacak_kisi_telefon_no'],
            satis_fiyati=data['satis_fiyati'],
            on_odeme_tutari=data['on_odeme_tutari'],
            odeme_tarihi=data['odeme_tarihi'],
            pesinat_tutari=data['pesinat_tutari'],
            pesinat_tarihi=data['pesinat_tarihi'],
            odeme_turu = odeme_yontemi,
            m2_birim_fiyati=data['m2_birim_fiyati'],
            aciklama_bigisi=data['aciklama_bigisi'],
            ek_bilgiler=data['ek_bilgiler']
        )

            satis_takip.save()



            user = User.objects.get(pk=request.user.id)


            parcel_user_history = ParcelUserHistory(
                parcel= parcel,
                user=user,
                # tarih="",
                islem="ekle")

            parcel_user_history.save()


            parcel.user_id = request.user.id  # Yeni kullanıcı ID'sini ayarlayın
            parcel.durum = "beklemede"  # Yeni kullanıcı ID'sini ayarlayın
            parcel.save()  # Değişikliği kaydedin


            return JsonResponse({'message': 'Veriler kaydedildi.'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Geçersiz JSON formatı.'}, status=400)
    else:
        return JsonResponse({'error': 'Yalnızca POST istekleri kabul edilir.'}, status=405)
    





@csrf_protect
def parcel_waiting(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            parcel = Parcel.objects.get(pk=data["parcel_id"])  # Örnek olarak bir parcel nesnesi alın
            parcel.durum = "kısa_bekleme"  # Yeni kullanıcı ID'sini ayarlayın
            
            
           
            now = timezone.now()  


            parcel.user_id = request.user.id
            parcel.bekleme_suresi_baslangic = now + timedelta(minutes=180)
            parcel.bekleme_suresi_bitisi = now + timedelta(minutes=240)
            parcel.bekleten_kullanici =  f"{request.user.first_name} {request.user.last_name}"

            parcel.save()  # Değişikliği kaydedin

            return JsonResponse({'message': 'Veriler kaydedildi.'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Geçersiz JSON formatı.'}, status=400)
    else:
        return JsonResponse({'error': 'Yalnızca POST istekleri kabul edilir.'}, status=405)
    

@csrf_protect
def parcel_waiting_remove(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            parcel = Parcel.objects.get(pk=data["parcel_id"])  # Örnek olarak bir parcel nesnesi alın
            
    

            parcel.durum = 'uygun'
            parcel.bekleme_suresi_baslangic = None  # Null yapma
            parcel.bekleme_suresi_bitisi = None  # Null yapma
            parcel.bekleten_kullanici = "None"  # Null yapma
            parcel.user_id = "None"  # Null yapma
            

            parcel.save()  # Değişikliği kaydedin

            return JsonResponse({'message': 'Veriler kaydedildi.'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Geçersiz JSON formatı.'}, status=400)
    else:
        return JsonResponse({'error': 'Yalnızca POST istekleri kabul edilir.'}, status=405)
    

