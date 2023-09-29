from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponse
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


from django.contrib.auth.decorators import user_passes_test


# Erişim kontrolü fonksiyonu
def is_user_history(user):
    return user.groups.filter(name='Kullanici_Islem_Gecmisi').exists()




# Kullanıcı editörler grubuna aitse bu sayfaya erişebilir
@user_passes_test(is_user_history)
def user_history_view(request):
    current_user = request.user
    



    return render(request, 'user_history.html', {'current_user': current_user})
