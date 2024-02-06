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
]