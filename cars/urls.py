from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns =[
    path('', CarList.as_view(), name='car_list'),
    path('<int:pk>/detail', CarDetail.as_view(), name='car_detail'),
]