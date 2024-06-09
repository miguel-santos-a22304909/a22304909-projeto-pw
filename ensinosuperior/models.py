from django.db import models

# Create your models here.

class Curso (models.Model):
    nome = models.CharField(max_length = 100)
    apresentacao = models.TextField(blank = True, null = True)
    objetivos = models.TextField(blank = True, null = True)
    competencias = models.TextField(blank = True, null = True)
    horas_contacto_total = models.CharField(max_length = 10)
    ects = models.IntegerField()

    def __str__(self):
        return f'{self.nome}'


class AreaCientifica (models.Model):
    nome = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.nome}'


class Disciplina (models.Model):
    nome = models.CharField(max_length = 100)
    ramo = models.CharField(max_length = 100)
    ano =  models.IntegerField()
    semestre = models.CharField(max_length = 15)
    ects = models.IntegerField()
    horas_contacto = models.CharField(max_length = 10)
    curricularIUnitReadableCode = models.CharField(max_length = 100)
    cursos = models.ManyToManyField(Curso, related_name = 'disciplinas')
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete = models.CASCADE, related_name = 'disciplinas', null = True)

    def __str__(self):
        return f'{self.nome}'

class Projeto (models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField(blank = True, null = True)
    conceitos_aplicados = models.TextField(blank = True, null = True)
    link_video = models.URLField(max_length = 200, null = True)
    link_github = models.URLField(max_length = 200, null = True)
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE, related_name = 'projeto',null = True)

    def __str__(self):
        return f'{self.nome}'


class LinguagemProgramacao (models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField(blank = True, null = True)
    projetos = models.ManyToManyField(Projeto ,related_name = 'linguagem_programacao')

    def __str__(self):
        return f'{self.nome}'


class Docente (models.Model):
    nome = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100, null=True)
    disciplinas = models.ManyToManyField(Disciplina, related_name = 'docentes')
