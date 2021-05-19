from django.db import models

# Create your models here.
class Profissional(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    espec_choices = (
        ('Cirurgião', 'Cirurgião'),
        ('Fisioterapeuta', 'Fisioterapeuta'),
        ('Cardiologista', 'Cardiologista'),
        ('Pediatra', 'Pediatra'),
        ('Radiologista', 'Radiologista'),
        ('Ortopedista', 'Ortopedista'),
        ('Enfermeiro', 'Enfermeiro'),
        ('Técnico de Enfermagem', 'Técnico de Enfermagem')
    )
    especialidade = models.CharField(max_length=50, choices=espec_choices)
    cpf = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome
