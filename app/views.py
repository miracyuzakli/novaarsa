
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from rest_framework import generics
from .models import Parcel, SatisTakipModel, ParcelUserHistory
from .serializers import ParcelSerializer, ParcelUserHistorySerializer, SatisTakipModelSerializer


@login_required
def index_view(request):
    current_user = request.user

    print(current_user)
    
    return render(request, 'index.html', {'current_user': current_user})





def login_view(request):

    if request.user.is_authenticated:
        return redirect('index') 
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            print(username)
            print(password)
            if user is not None:
                login(request, user)
                return redirect('index')  
            else:
                error_message = 'Geçersiz kullanıcı adı veya şifre'
                return render(request, 'login.html', {'error_message': error_message})
        else:
            return render(request, 'login.html')



def logout_view(request):
    
    logout(request)
    print("Çıkış yapıldı")
    return redirect('index') 






#! Applications


from rest_framework import viewsets
from .models import Parcel
from .serializers import ParcelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ParcelFilter, ParcelUserHistoryFilter, SatisTakipModelFilter
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json
from rest_framework.decorators import action
from rest_framework.response import Response





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
    





@login_required
def dashboard_view(request):
    current_user = request.user

    print(current_user)
    
    return render(request, 'user_dashbord.html', {'current_user': current_user})







@csrf_protect
def approve_parcels(request):
        
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            parcel_id = data.get("parcel_id")
            new_status = data.get("durum")

            # Parçayı veritabanından alın
            parcel = Parcel.objects.get(pk=parcel_id)

            # Yeni değerleri atayın
            parcel.durum = new_status

            # Parçayı kaydedin
            parcel.save()



            parcel_user_history = ParcelUserHistory(
                parcel= parcel,
                user_id=request.user.id,
                # tarih="",
                islem="onay")

            parcel_user_history.save()

            return JsonResponse({'message': 'Veriler kaydedildi.'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Geçersiz JSON formatı.'}, status=400)
    else:
        return JsonResponse({'error': 'Yalnızca POST istekleri kabul edilir.'}, status=405)
    



@csrf_protect
def remove_parcels(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            parcel_id = data.get("parcel_id")
            new_status = data.get("durum")
            new_user_id = data.get('user_id');
            # Parçayı veritabanından alın
            parcel = Parcel.objects.get(pk=parcel_id)

            # Yeni değerleri atayın
            parcel.durum = new_status
            parcel.user_id = new_user_id

            # Parçayı kaydedin
            parcel.save()

            parcel_user_history = ParcelUserHistory(
                parcel= parcel,
                user_id=request.user.id,
                # tarih="",
                islem="çıkar")

            parcel_user_history.save()


            return JsonResponse({'message': 'Veriler kaydedildi.'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Geçersiz JSON formatı.'}, status=400)
    else:
        return JsonResponse({'error': 'Yalnızca POST istekleri kabul edilir.'}, status=405)