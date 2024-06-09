#bandas models.py
from django.db import models

# Create your models here.

class Banda (models.Model):
    nome = models.CharField(max_length = 100)
    foto = models.ImageField(null = True)
    descricao = models.TextField(blank = True, null = True)
    nacionalidade = models.CharField(max_length = 100, null = True)
    ano_criacao = models.IntegerField(null = True)

    def __str__(self):
        return f'{self.nome}'

class Album (models.Model):
    titulo = models.CharField(max_length = 100)
    capa = models.ImageField(upload_to="capas", null=True, blank=True, default=None)
    banda = models.ForeignKey(Banda, on_delete = models.CASCADE, related_name = 'albuns')

    def __str__(self):
        return f'{self.banda} - {self.titulo}'


class Musica (models.Model):
    titulo = models.CharField(max_length = 100)
    duracao = models.CharField(max_length = 10 , verbose_name = 'Duração', default = "0")
    link_spotify = models.URLField(max_length = 200, null = True, blank=True)
    banda = models.ForeignKey(Banda, on_delete = models.CASCADE, related_name = 'musicas')
    album = models.ForeignKey(Album, on_delete = models.CASCADE, related_name = 'musicas')
    letra = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return f'{self.banda} - {self.titulo}'





