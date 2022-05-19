from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50, default='')
    direccion = models.CharField(max_length=50, default='')
    telefono = models.CharField(max_length=20, default='')
