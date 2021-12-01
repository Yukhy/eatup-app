from django.urls import path, include
from . import views

app_name = 'eatup'

urlpatterns = [
    path('', views.index, name='index'),
    path('shopping-cart/', views.shopping_cart, name='shopping-cart'),
    path('notification/', views.notification, name='notification'),
    path('user-info/', views.user_info, name='user-info'),
    path('scan/', views.scan, name='scan'),

    # api
    path('api/scan-item/', views.api_scan_item, name='api-scan-item'),
]
