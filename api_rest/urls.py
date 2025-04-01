from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_places, name='get_all_places'),
    path('create/', views.create_place, name='create_place'),
    path('<str:place_name>/', views.edit_place, name='edit-place'),
    path('<str:place_name>/', views.get_place_by_name, name='get_place_by_name'),
]
