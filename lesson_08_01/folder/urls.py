import imp
from . import views
from django.urls import path

urlpatterns = [
    path('animals/', views.AnimalList.as_view(), name='animal_list'),
    path('animals/<int:pk>', views.AnimalDetail.as_view(), name='animal_detail'),
    path('animals/create/', views.AnimalCreate.as_view(), name='animal_create'),
    path('animals/<int:pk>/update', views.AnimalUpdate.as_view(), name='animal_update'),
    path('animals/<int:pk>/delete', views.AnimalDelete.as_view(), name='animal_delete'),

    path('enclosures/', views.EnclosureList.as_view(), name='enclosure_list'),
    path('enclosures/<int:pk>', views.EnclosureDetail.as_view(), name='enclosure_detail'),
    path('enclosures/create/', views.EnclosureCreate.as_view(), name='enclosure_create'),
    path('enclosures/<int:pk>/update', views.EnclosureUpdate.as_view(), name='enclosure_update'),
    path('enclosures/<int:pk>/delete', views.EnclosureDelete.as_view(), name='enclosure_delete'),

    path('cars/', views.CarList.as_view(), name='car_list'),
    path('cars/<int:pk>', views.CarDetail.as_view(), name='car_detail'),
    path('cars/create/', views.CarCreate.as_view(), name='car_create'),
    path('cars/<int:pk>/update', views.CarUpdate.as_view(), name='car_update'),
    path('cars/<int:pk>/delete', views.CarDelete.as_view(), name='car_delete'),

    path('clients/', views.ClientList.as_view(), name='client_list'),
    path('clients/<int:pk>', views.ClientDetail.as_view(), name='client_detail'),
    path('clients/create/', views.ClientCreate.as_view(), name='client_create'),
    path('clients/<int:pk>/update', views.ClientUpdate.as_view(), name='client_update'),
    path('clients/<int:pk>/delete', views.ClientDelete.as_view(), name='client_delete'),
]