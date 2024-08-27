from django.contrib import admin
from .models import *
# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'email', 'cidade', 'sexo')

admin.site.register(Aluno, AlunoAdmin)