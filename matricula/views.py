from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def AlunoForm(request):
    if request.method == "POST":
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("kkjkj")
        
    else:
         form = AlunoForm()
    
    context = {
        'form': form
    }

    return render(request, "aluno_login.html", context)