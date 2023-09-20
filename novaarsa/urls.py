from django.contrib import admin
from django.urls import path
from app.views import login_view, index_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('index/', index_view, name='index'),
    path('logout/', logout_view, name='logout'),

]
