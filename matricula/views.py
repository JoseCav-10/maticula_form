from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.


def index(request):
    
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listagem")
        
    else:
         form = AlunoForm()
    
    context = {
        'form': form
    }

    return render(request, "aluno_login.html", context=context)

def listagem(request):
    alunos = Aluno.objects.all()

    context = {
        "list_alunos": alunos 
    }

    return render(request, "listagem.html", context=context)

'''def AlunoForm(request):
    if request.method == "POST":
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listagem")
        
    else:
         form = AlunoForm()
    
    context = {
        'form': form
    }

    return render(request, "aluno_login.html", context)'''