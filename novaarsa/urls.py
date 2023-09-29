from django.contrib import admin
from django.urls import path, include
from app.views import (
    login_view,
    index_view,
    logout_view,
    ParcelViewSet,
    ParcelUserHistoryViewSet,
    save_form_data,
    SatisTakipModelViewSet,
    dashboard_view,
    remove_parcels,
    approve_parcels,
    user_history_view

)
from rest_framework.routers import DefaultRouter


routerParcel = DefaultRouter()
routerParcel.register(r"parcels", ParcelViewSet)

routerParcelUserHistory = DefaultRouter()
routerParcelUserHistory.register(r"parcels-user-history", ParcelUserHistoryViewSet)

routerParcelUserHistory = DefaultRouter()
routerParcelUserHistory.register(r"parcels-user-history", ParcelUserHistoryViewSet)


routerSatisTakipModel = DefaultRouter()
routerSatisTakipModel.register(r"satis-takip", SatisTakipModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),


    
    path("", login_view, name="login"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    
    path("index/", index_view, name="index"),
    path("dashboard/", dashboard_view, name="dashboard"),


    path("", include(routerParcel.urls)),
    path("", include(routerParcelUserHistory.urls)),
    path("", include(routerSatisTakipModel.urls)),


    path("save-form-data/", save_form_data, name="save_form_data"),
    path("remove-parcel-user-list/", remove_parcels, name="remove_parcels"),
    path("approve-parcel-user-list/", approve_parcels, name="approve_parcel_user_list"),




    path("user-parcels-history/", user_history_view, name="user_parcels_history")
]
