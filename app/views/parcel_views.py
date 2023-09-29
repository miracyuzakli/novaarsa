
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from ..models import Parcel, SatisTakipModel, ParcelUserHistory
from ..serializers import ParcelSerializer, ParcelUserHistorySerializer, SatisTakipModelSerializer
from ..filters import ParcelFilter, ParcelUserHistoryFilter, SatisTakipModelFilter

from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json
from rest_framework.decorators import action
from rest_framework.response import Response








#! Applications







class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ParcelFilter
  

class ParcelUserHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParcelUserHistory.objects.all()
    serializer_class = ParcelUserHistorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ParcelUserHistoryFilter


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

            print("#"*10)
            print(data["parsel_id"])

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





            parcel_user_history = ParcelUserHistory(
                parcel= parcel,
                user_id=request.user.id,
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
    





