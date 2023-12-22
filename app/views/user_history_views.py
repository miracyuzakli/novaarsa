from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from ..models import Parcel, SatisTakipModel, ParcelUserHistory
from ..serializers import (
    ParcelSerializer)
from ..filters import ParcelFilter

from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json
from rest_framework.decorators import action
from rest_framework.response import Response


from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.contrib.auth.models import User


# Erişim kontrolü fonksiyonu
def is_user_history(user):
    return user.groups.filter(name="user_history").exists()


# Kullanıcı editörler grubuna aitse bu sayfaya erişebilir
@user_passes_test(is_user_history)
def user_history_view(request):
    current_user = request.user

    return render(request, "user_history.html", {"current_user": current_user})





from django.http import JsonResponse
import json

@csrf_protect
def get_user_history_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            filter_start_date = data["filter_start_date"]
            filter_end_date = data["filter_end_date"]
            filter_username = data["filter_username"]
            # filter_parcel = data["filter_parcel"]
            filter_parcel = "all"
            if filter_parcel == "all":
                matching_parcels = Parcel.objects.all()
            else:
                matching_parcels = Parcel.objects.filter(mevki=filter_parcel)
            

            if filter_username == "all":
                matching_users = User.objects.all()
            else:
                matching_users = User.objects.filter(id=filter_username)

            if filter_start_date == "" or filter_end_date == "":
            # Bu parcel_id'leri kullanarak ParcelUserHistory modelini filtrele
                history_data = ParcelUserHistory.objects.filter(
                    parcel__in=matching_parcels,
                    user_id__in=matching_users,

                )
            else:
                # Bu parcel_id'leri kullanarak ParcelUserHistory modelini filtrele
                history_data = ParcelUserHistory.objects.filter(
                    tarih__range=[filter_start_date, filter_end_date],
                    parcel__in=matching_parcels,
                    user_id__in=matching_users,

                )

            # JSON yanıt olarak geçmiş verileri döndür
            history_data_list = [
                {
                    
                    "il": item.parcel.il,
                    "ilce": item.parcel.ilce,
                    "mevki": item.parcel.mevki,
                    "ada": item.parcel.ada,
                    "parcel": item.parcel.parsel,
    
                    "user_id": item.user_id,
                    "tarih": item.tarih.strftime('%Y-%m-%d'),
                    "saat": item.saat.strftime('%H:%M:%S'),
                    "islem": item.islem,


                    "first_name": item.user.first_name,
                    "last_name": item.user.last_name,
                    "user_email": item.user.email

                }
                for item in history_data
            ]

            return JsonResponse({"history_data": history_data_list}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Geçersiz JSON formatı."}, status=400)
    else:
        return JsonResponse(
            {"error": "Yalnızca POST istekleri kabul edilir."}, status=405
        )
