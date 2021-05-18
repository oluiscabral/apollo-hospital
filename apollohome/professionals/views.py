from django.shortcuts import render
from patients.models import Paciente
from floors.models import Andar
from .models import Profissional
# Create your views here.

def dashboard_view(request):
    user = request.user
    
    lista_pacientes = Paciente.objects.all()
    lista_profissionais = Profissional.objects.all()
    lista_andares = Andar.objects.all()

    context = {
        'lista_pacientes': lista_pacientes,
        'lista_profissionais': lista_profissionais,
        'lista_andares': lista_andares,
        'user': user
    }

    return render(request, '../templates/dashboard/dashboard.html', context)