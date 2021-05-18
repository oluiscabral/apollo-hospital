from django.db import models
from professionals.models import Profissional

# Create your models here.
class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField(null=True)
    estado_atendimento = models.BooleanField(default=False)
    cpf = models.CharField(max_length=14)
    atend_desc = models.CharField(max_length=500)
    profResponsavel = models.OneToOneField(Profissional, on_delete=models.CASCADE)