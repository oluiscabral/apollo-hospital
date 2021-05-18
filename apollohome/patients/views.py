from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Paciente


def patients(request):
    return render(request, '../templates/dashboard/dashboard.html', {'table': Paciente.objects.all()})
