

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from ..models import Parcel, ParcelPricing, SatisTakipModel, ParcelUserHistory
from ..serializers import ParcelSerializer, ParcelPricingSerializer
from ..filters import ParcelFilter, ParcelPricingFilter

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





@login_required
def parcesl_edits(request):
    current_user = request.user

    
    return render(request, 'parcels-edits.html', {'current_user': current_user})







@csrf_protect
def set_parcel_price(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            parcel = Parcel.objects.get(pk=data["parcel_id"])  # Örnek olarak bir parcel nesnesi alın

            parcel.fiyat = data["new_price"]
           

            parcel.save()  # Değişikliği kaydedin

            return JsonResponse({'message': 'Veriler kaydedildi.'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Geçersiz JSON formatı.'}, status=400)
    else:
        return JsonResponse({'error': 'Yalnızca POST istekleri kabul edilir.'}, status=405)