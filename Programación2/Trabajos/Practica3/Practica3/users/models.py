from django.db import models

# Create your models here.


class usuarios(models.Model):
    nickname = models.CharField(max_length = 10)
    email = models.EmailField()
    CUI = models.IntegerField()
