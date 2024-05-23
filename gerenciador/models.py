from typing import Any
from django.db import models

# Create your models here.

class Aluno(models.Model):
   primeiro_nome = models.CharField(max_length=40)
   sobrenome = models.CharField(max_length=80)
   email = models.EmailField(max_length=100)
   cpf = models.CharField(max_length=11,unique=True)
   data_de_nascimento = models.DateField()
   
   pass
