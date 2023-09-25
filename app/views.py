
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from rest_framework import generics
from .models import Parcel
from .serializers import ParcelSerializer




@login_required
def index_view(request):

    return render(request, 'index.html')





def login_view(request):
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
from .filters import ParcelFilter


class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ParcelFilter






# myapp/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json

@csrf_protect
def save_form_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            # Verileri işleyin ve konsola yazdırın
            print(data)
            return JsonResponse({'message': 'Veriler kaydedildi.'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Geçersiz JSON formatı.'}, status=400)
    else:
        return JsonResponse({'error': 'Yalnızca POST istekleri kabul edilir.'}, status=405)
