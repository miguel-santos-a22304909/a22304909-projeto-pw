from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Curso)
admin.site.register(AreaCientifica)
admin.site.register(Disciplina)
admin.site.register(Projeto)
admin.site.register(LinguagemProgramacao)
admin.site.register(Docente)