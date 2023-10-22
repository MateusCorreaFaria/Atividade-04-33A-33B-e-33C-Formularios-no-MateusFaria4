# https://docs.djangoproject.com/en/4.2/topics/db/models/

from django.db import models


class carros(models.Model):
    nome = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=70)
    automatico_manual = models.CharField(max_length=20)
    data_fabricação = models.DateField()


class videogames(models.Model):
    nome = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    estilo = models.CharField(max_length=50)
    data_lançamento = models.DateField()
