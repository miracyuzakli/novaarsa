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
    get_sales_tracking_form_data,

    # Parcel Edits
    parcesl_edits,
    set_parcel_price,
    add_parcel_data,

    # Users
    users_views,
    user_groups,
    set_user_operations,
    check_user_groups,
    set_waiting_counter,
get_current_user_waiting_count,
set_user_parcel_waiting_permit

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
    path("get-user-history-data/", get_user_history_data, name="get_user_history_data"),




    # Parcel Edits
    path("parcels-edit/", parcesl_edits, name="parcels_edit"),
    path("set-parcel-price/", set_parcel_price),
    path("add-parcel-data/", add_parcel_data),
    


    # Users
    path("users/", users_views, name="users_views"),
    path("get-users-groups/", user_groups),
    path("set-users-groups/", set_user_operations),
    path("set-users-waiting-count/", set_waiting_counter),
    path("get-current-user-groups/", check_user_groups),
    path('get-current-user-waiting-count/', get_current_user_waiting_count),
    path('set-user-parcel-waiting-permit/', set_user_parcel_waiting_permit),


    




]
