from django.db import models

# Create your models here.


class Aluno(models.Model):

    CURSO_CHOICES = (
        ('informatica',"informatica"),
        ('alimentos',"alimentos"),
        ('apicultura', 'apicultura')
    )

    CIDADE_CHOICES = (
        ('Pe',"Pereiro"),
        ('Pf',"Pau dos Ferros"),
        ('Er', 'Ereré'),
        ('Sm', "São Miguel")
    )

    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    email = models.EmailField()
    cidade = models.CharField(choices=CIDADE_CHOICES,max_length=255, default="")
    curso = models.CharField(choices=CURSO_CHOICES,max_length=30,default='')