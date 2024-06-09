from django.db import models

# Create your models here.

class Autor (models.Model):
    username = models.CharField(max_length = 100)
    foto_perfil = models.ImageField(null = True, blank = True, verbose_name = 'Foto de Perfil')
    descricao = models.TextField(verbose_name = 'Descrição', default = ' ')

    def __str__(self):
        return self.username

class Artigo (models.Model):
    titulo = models.CharField(max_length = 100)
    imagem = models.ImageField(null = True, blank = True)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE, related_name = 'artigos')
    descricao = models.TextField(verbose_name = 'Descrição')
    likes = models.IntegerField(default = 0)

    FRACO = 1
    INSUFICIENTE = 2
    SUFICIENTE = 3
    BOM = 4
    MUITO_BOM = 5
    RATING_CHOICES = [
        (FRACO, '1'),
        (INSUFICIENTE, '2'),
        (SUFICIENTE, '3'),
        (BOM, '4'),
        (MUITO_BOM, '5'),
        ]
    rating = models.IntegerField(choices = RATING_CHOICES, blank = True, null = True)

    def __str__(self):
        return self.titulo



class Comentario (models.Model):
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE, related_name = 'comentarios', null = True)
    texto = models.TextField()
    likes = models.IntegerField(default = 0)
    artigo = models.ForeignKey(Artigo, on_delete = models.CASCADE, related_name = 'comentarios')

    def __str__(self):
        return f'Autor do comentário: {self.autor} | Artigo: {self.artigo}'