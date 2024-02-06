from django.shortcuts import render
from sre_constants import SUCCESS
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from .models import Animal, Enclosure

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
