

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
    



@csrf_protect
def add_parcel_data(request):
    if request.method == 'POST':

        try:
            data = json.loads(request.body.decode('utf-8'))
            print(data);

            # Formdan gelen verileri al
            il = data['il']
            ilce = data['ilce']
            mevki = data['mevki']
            ada = data['ada']
            parsel = data['parsel']
            m2_net =data['m2_net']
            fiyat = data['fiyat']
            durum =  'uygun' 
            user_id = 'None'
            bekleme_suresi_baslangic = None
            bekleme_suresi_bitisi =  None
            bekleten_kullanici = 'None'

            # Veriyi veritabanına kaydet
            new_parcel = Parcel(
                il=il,
                ilce=ilce,
                mevki=mevki,
                ada=ada,
                parsel=parsel,
                m2_net=m2_net,
                fiyat=fiyat,
                durum=durum,
                user_id=user_id,
                bekleme_suresi_baslangic=bekleme_suresi_baslangic,
                bekleme_suresi_bitisi=bekleme_suresi_bitisi,
                bekleten_kullanici=bekleten_kullanici
            )
            new_parcel.save()

        # Başka bir sayfaya yönlendir
            return JsonResponse({'message': 'Veriler kaydedildi.'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Geçersiz JSON formatı.'}, status=400)
    else:
        return JsonResponse({'error': 'Yalnızca POST istekleri kabul edilir.'}, status=405)






from django.http import JsonResponse
import pandas as pd
from ..models import Parcel

# def parcel_upload_file_view(request):
#     if request.method == 'POST':
#         excel_file = request.FILES.get('file')

#         # Excel veya CSV dosyasını okuyun
#         if excel_file.name.endswith('.xlsx'):
#             df = pd.read_excel(excel_file)
#         elif excel_file.name.endswith('.csv'):
#             df = pd.read_csv(excel_file)
#         else:
#             return JsonResponse({'error': 'Geçersiz dosya formatı'}, status=400)
        
#         print(df)

#         # temp_columns = ["İL",	"İLÇE",	"MEVKİ"	,"ADA"	,"PARSEL"	,"M2 NET"	,"FİYAT"]
#         # if df.columns.value == temp_columns:
#         for _, row in df.iterrows():
#             # Formdan gelen verileri al
#             il = row['İL']
#             ilce = row['İLÇE']
#             mevki = row['MEVKİ']
#             ada = row['ADA']
#             parsel = row['PARSEL']
#             m2_net =row['M2 NET']
#             fiyat = row['FİYAT']
#             durum =  'uygun' 
#             user_id = 'None'
#             bekleme_suresi_baslangic = None
#             bekleme_suresi_bitisi =  None
#             bekleten_kullanici = 'None'

#             # Veriyi veritabanına kaydet
#             new_parcel = Parcel(
#                 il=il,
#                 ilce=ilce,
#                 mevki=mevki,
#                 ada=ada,
#                 parsel=parsel,
#                 m2_net=m2_net,
#                 fiyat=fiyat,
#                 durum=durum,
#                 user_id=user_id,
#                 bekleme_suresi_baslangic=bekleme_suresi_baslangic,
#                 bekleme_suresi_bitisi=bekleme_suresi_bitisi,
#                 bekleten_kullanici=bekleten_kullanici
#             )
#             new_parcel.save()
#             print(row)

#         return JsonResponse({'message': 'Dosya başarıyla işlendi'})

#     return JsonResponse({'error': 'Geçersiz istek'}, status=400)






from django.http import JsonResponse
import pandas as pd
import traceback


def parcel_upload_file_view(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('file')

        try:
            if excel_file.name.endswith('.csv'):
                df = pd.read_csv(excel_file)
                print(df)
            else:
                return JsonResponse({'error': 'Geçersiz dosya formatı'}, status=400)
            
            temp_columns = ["İL",	"İLÇE",	"MEVKİ"	,"ADA"	,"PARSEL"	,"M2 NET"	,"FİYAT", "SATIŞ DURUMU", "MENUNAME"]
                            # "İL   İLÇE    MEVKİ    ADA  PARSEL  M2 NET    FİYAT SATIŞ DURUMU     MENUNAME"
            df_columns = list(df)
            print(df_columns)
            if df_columns == temp_columns:

                for _, row in df.iterrows():
                # Formdan gelen verileri al
                    il = row['İL']
                    ilce = row['İLÇE']
                    mevki = row['MEVKİ']
                    ada = row['ADA']
                    parsel = row['PARSEL']
                    m2_net =row['M2 NET']
                    fiyat = row['FİYAT']
                    menu_name = row["MENUNAME"]
                    durum =  row["SATIŞ DURUMU"] 
                    user_id = 'None'
                    bekleme_suresi_baslangic = None
                    bekleme_suresi_bitisi =  None
                    bekleten_kullanici = 'None'

                    # Veriyi veritabanına kaydet
                    new_parcel = Parcel(
                        il=il,
                        ilce=ilce,
                        mevki=mevki,
                        ada=ada,
                        parsel=parsel,
                        m2_net=m2_net,
                        fiyat=fiyat,
                        durum=durum,
                        menu_name = menu_name,
                        user_id=user_id,
                        bekleme_suresi_baslangic=bekleme_suresi_baslangic,
                        bekleme_suresi_bitisi=bekleme_suresi_bitisi,
                        bekleten_kullanici=bekleten_kullanici
                    )
                    new_parcel.save()

                return JsonResponse({'message': 'Dosya başarıyla işlendi'})
            else:
                return JsonResponse({'message': 'Dosya Formatı uygun değil!!!'})


        except Exception as e:
            traceback.print_exc()  # Hata detaylarını konsola yazdır
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Geçersiz istek'}, status=400)
