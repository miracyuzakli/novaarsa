
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout






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
