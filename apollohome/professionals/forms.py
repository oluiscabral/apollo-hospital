from django import forms
from .models import Profissional

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = {
            'nome',
            'cpf',
            'especialidade',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'nameInput', 'required': True}),
            'cpf': forms.TextInput(attrs={'class': 'cpfInput', 'required': True}),
            'especialidade': forms.Select(attrs={'class': 'especInput', 'required': True})
        }