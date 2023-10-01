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



@login_required
def dashboard_view(request):
    current_user = request.user

    
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

            user = User.objects.get(pk=request.user.id)


            parcel_user_history = ParcelUserHistory(
                parcel= parcel,
                user=user,
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

            user = User.objects.get(pk=request.user.id)

            parcel_user_history = ParcelUserHistory(
                parcel= parcel,
                user=user,
                # tarih="",
                islem="çıkar")

            parcel_user_history.save()


            satis_takip = SatisTakipModel.objects.get(parcel_id=parcel_id)  
            satis_takip.delete()



            return JsonResponse({'message': 'Veriler kaydedildi.'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Geçersiz JSON formatı.'}, status=400)
    else:
        return JsonResponse({'error': 'Yalnızca POST istekleri kabul edilir.'}, status=405)
    


# @csrf_protect
# def edit_parcel_forms(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body.decode('utf-8'))

#             parcel_id = data.get("parcel_id")
#             new_status = data.get("durum")
#             new_user_id = data.get('user_id');
#             # Parçayı veritabanından alın
#             parcel = Parcel.objects.get(pk=parcel_id)



#             return JsonResponse({'message': 'Veriler kaydedildi.'}, status=200)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Geçersiz JSON formatı.'}, status=400)
#     else:
#         return JsonResponse({'error': 'Yalnızca POST istekleri kabul edilir.'}, status=405)