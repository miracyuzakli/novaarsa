from django.contrib import admin
from django.urls import path, include
from app.views import login_view, index_view, logout_view, ParcelViewSet, save_form_data
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'parcels', ParcelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('index/', index_view, name='index'),
    path('logout/', logout_view, name='logout'),

    path('', include(router.urls)),
    path('save-form-data/', save_form_data, name='save_form_data'),


]
