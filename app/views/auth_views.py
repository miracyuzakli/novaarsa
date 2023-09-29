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