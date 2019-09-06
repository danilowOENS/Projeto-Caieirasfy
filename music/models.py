from django.db import models

# Create your models here.
from django.forms import CharField


class Musica(models.Model):
    nome_da_musica = models.CharField(max_length=255)
    artista = models.CharField(max_length=255)
    genero_musical = models.CharField(max_length=255)
    link_musica = models.CharField(max_length=255)

c