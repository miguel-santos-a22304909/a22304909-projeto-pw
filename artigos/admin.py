from django.contrib import admin

from .models import Autor
from .models import Artigo
from .models import Comentario
# Register your models here.

admin.site.register(Autor)
admin.site.register(Artigo)
admin.site.register(Comentario)