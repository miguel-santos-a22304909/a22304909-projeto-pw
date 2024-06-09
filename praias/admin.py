from django.contrib import admin

from .models import Praia
from .models import Regiao
from .models import Servico

# Register your models here.

admin.site.register(Praia)
admin.site.register(Regiao)
admin.site.register(Servico)