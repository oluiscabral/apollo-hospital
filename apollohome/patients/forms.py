from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = {
            'nome',
            'cpf',
            'idade',
            'estado_atendimento',
            'atend_desc',
            'profResponsavel'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'nameInput', 'required': True}),
            'cpf': forms.TextInput(attrs={'class': 'cpfInput', 'required': True}),
            'idade': forms.NumberInput(attrs={'class': 'idadeInput', 'required': True}),
            'estado_atendimento': forms.CheckboxInput(attrs={'class': 'estadoInput'}),
            'atend_desc': forms.TextInput(attrs={'class': 'descInput', 'required': True}),
            'profResponsavel': forms.Select(attrs={'class': 'profInput', 'required': True})

        }