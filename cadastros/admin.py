from django.contrib import admin

from .models import Atividade, Avaliacao, Campo

# Register your models here.
admin.site.register(Atividade)
admin.site.register(Campo)
admin.site.register(Avaliacao)
