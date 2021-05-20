from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Paciente

from .forms import PacienteForm

def patientsCreate_view(request):
    
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = PacienteForm()

    context = {
        'form': form
    }   
    return render(request,'creationals/patient.html', context)