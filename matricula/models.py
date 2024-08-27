from django.db import models

# Create your models here.


class Aluno(models.Model):

    SEXO_CHOICES = (
        ('masculino',"masculino"),
        ('feminino',"feminino"),
        ('outro', 'outro')
    )

    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=15)
    email = models.EmailField()
    cidade = models.CharField(max_length=255)
    sexo = models.CharField(choices=SEXO_CHOICES,max_length=30,default='masculino')