from django.shortcuts import render
from sre_constants import SUCCESS
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest

from .models import Animal, Enclosure

from .models import Car, Client

class AnimalList(ListView):
    model = Animal
    context_object_name = 'animal_list'

class AnimalDetail(DetailView):
    model = Animal
    context_object_name = 'animal'

class AnimalCreate(CreateView):
    model = Animal
    fields = '__all__'
    success_url = reverse_lazy('animal_list')
    
class AnimalUpdate(UpdateView):
    model = Animal
    fields = '__all__'
    success_url = reverse_lazy('animal_list')
  
class AnimalDelete(DeleteView):
    model = Animal
    success_url = reverse_lazy('animal_list')
    template_name = 'Folder/animal_form.html'


class EnclosureList(ListView):
    model = Enclosure
    context_object_name = 'enclosure_list'

class EnclosureDetail(DetailView):
    model = Enclosure

class EnclosureCreate(CreateView):
    model = Enclosure
    fields = '__all__'
    success_url = reverse_lazy('enclosure')
    
class EnclosureUpdate(UpdateView):
    model = Enclosure
    fields = '__all__'
    success_url = reverse_lazy('enclosure')
  
class EnclosureDelete(DeleteView):
    model = Enclosure
    success_url = reverse_lazy('enclosure')
    template_name = 'Folder/enclosure_form.html'

class Other(TemplateView):
    template_name = 'about.html'


class CarList(ListView):
    model = Car
    context_object_name = 'car_list'

    def get_queryset(self):
        return super().get_queryset().filter(availability=True)

class CarDetail(DetailView):
    model = Car
    context_object_name = 'car'

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')

    def form_valid(self, form):
        year = form.cleaned_data['year']
        if year > 2024:
            return HttpResponse('year should be less then 2024')
        else:
            form.save()
            return HttpResponse('successful something')
    
class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')
  
class CarDelete(DeleteView):
    model = Car
    success_url = reverse_lazy('car_list')
    template_name = 'Folder/car_form.html'


class ClientList(ListView):
    model = Client
    context_object_name = 'client_list'

class ClientDetail(DetailView):
    model = Client
    context_object_name = 'client'

class ClientCreate(CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('client_list')
    
class ClientUpdate(UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('client_list')
  
class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')
    template_name = 'Folder/client_form.html'

