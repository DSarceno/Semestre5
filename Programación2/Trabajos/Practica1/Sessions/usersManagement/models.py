from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length = 15)
    apellido = models.CharField(max_length = 20)
    password = models.CharField(max_length = 15)
