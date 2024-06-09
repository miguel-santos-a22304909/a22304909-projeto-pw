from django.db import models

# Create your models here.

class Pessoa(models.Model):
    primeiro_nome = models.CharField(max_length = 50)
    ultimo_nome = models.CharField(max_length = 50)
    idade = models.IntegerField()

    def __str__(self):
        return f'{self.primeiro_nome} {self.ultimo_nome} - {self.idade} anos'