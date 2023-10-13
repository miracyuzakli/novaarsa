from django.contrib import admin
from django.urls import path, include
from app.views import (
    login_view,
    index_view,
    logout_view,
    get_users,
    ParcelViewSet,
    ParcelPricingFilterView,
    parcel_waiting,
    parcel_waiting_remove,
    save_form_data,
    edit_form_data,
    download_form_data_docx,
    dashboard_view,
    remove_parcels,
    approve_parcels,
    user_history_view,
    get_user_history_data,
    get_sales_tracking_form_data



)
from rest_framework.routers import DefaultRouter


routerParcel = DefaultRouter()
routerParcel.register(r"parcels", ParcelViewSet)



urlpatterns = [
    path("admin/", admin.site.urls),


    
    path("", login_view, name="login"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("get-users/", get_users, name="get_users"),

    
    path("index/", index_view, name="index"),
    path("dashboard/", dashboard_view, name="dashboard"),


    path("", include(routerParcel.urls)),
    path('parcel-pricing-filter/', ParcelPricingFilterView.as_view(), name='parcel-pricing-filter'),
    path("set-parcel-waiting/", parcel_waiting, name="set_parcel_waiting"),
    path("set-parcel-waiting-remove/", parcel_waiting_remove, name="set_parcel_waiting_remove"),

    path("get-sales-tracking-form-data/", get_sales_tracking_form_data),


    path("save-form-data/", save_form_data, name="save_form_data"),
    path("edit-form-data/", edit_form_data),
    path("remove-parcel-user-list/", remove_parcels, name="remove_parcels"),
    path("approve-parcel-user-list/", approve_parcels, name="approve_parcel_user_list"),
    path("download-form-data-docx/", download_form_data_docx, name="download_form_data_docx"),




    path("user-parcels-history/", user_history_view, name="user_parcels_history"),
    path("get-user-history-data/", get_user_history_data, name="get_user_history_data")
]
