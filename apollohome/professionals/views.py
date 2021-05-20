from django.shortcuts import render, redirect
from patients.models import Paciente
from floors.models import Andar
from .models import Profissional
from .forms import ProfissionalForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


def dashboard_view(request):
    user = request.user

    if not user.is_authenticated:
        return HttpResponseRedirect('login/')
        
    lista_pacientes = Paciente.objects.all()
    lista_profissionais = Profissional.objects.all()
    lista_andares = Andar.objects.all()

    leitos_totais = 0
    leitos_ocupados = 0
    for andar in lista_andares:
        leitos_ocupados+=andar.leitos_ocupados
        leitos_totais+=andar.leitos_totais

    porcentagem = round((leitos_ocupados/leitos_totais)*100, 1)
    
    context = {
        'lista_pacientes': lista_pacientes,
        'lista_profissionais': lista_profissionais,
        'lista_andares': lista_andares,
        'leitos_totais': leitos_totais,
        'leitos_ocupados': leitos_ocupados,
        'porcentagem': porcentagem,
        'user': user
    }

    return render(request, 'dashboard/dashboard.html', context)


def professionalCreate_view(request):
    
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = ProfissionalForm()

    context = {
        'form': form
    }   
    return render(request,'creationals/profissional.html', context)

def login(request):
    return render(request, 'registration/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = { 
        'form' : form
    }
    return render(request, 'registration/register.html', context)
