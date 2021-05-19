from django.shortcuts import render
from patients.models import Paciente
from floors.models import Andar
from .models import Profissional
from .forms import ProfissionalForm
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


def professionalCreate_view(request):
    
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = ProfissionalForm()

    context = {
        'form': form
    }   
    return render(request,'index/index.html', context)