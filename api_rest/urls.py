from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_places, name='get_all_places'),
    path('<str:name>', views.get_place_by_name, name='get_place_by_name')
]
