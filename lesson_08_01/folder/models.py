from django.db import models

# Create your models here.

class Animal(models.Model):
    Health_status = (('h', 'Здоровый'), ('s', 'Больной'), ('n', 'Не обследованный' ))
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50, null=True, blank=True)
    health_status = models.CharField(max_length=1, choices=Health_status, default='h')


class Enclosure(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    animals = models.ManyToManyField('Animal')
