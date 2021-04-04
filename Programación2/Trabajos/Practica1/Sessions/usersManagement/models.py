from django.db import models

# Create your models here.

class usuarios(models.Model):
    email = models.EmailField()
    nickname = models.CharField(max_length = 10)
    nombre = models.CharField(max_length = 15)
    apellido = models.CharField(max_length = 20)
    sexo = models.CharField(max_length = 9)
    carrera = models.CharField(max_length = 30)
    password = models.CharField(max_length = 15)
