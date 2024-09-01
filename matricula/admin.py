from django.contrib import admin
from .models import *
# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'email', 'cidade', 'curso')

admin.site.register(Aluno, AlunoAdmin)