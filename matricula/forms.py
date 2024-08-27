from django import forms
from .models import *

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"
