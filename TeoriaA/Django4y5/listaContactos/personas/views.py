from django.shortcuts import render
from .models import Persona

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/lista.html', {'personas': personas})