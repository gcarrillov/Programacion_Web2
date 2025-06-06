from django.shortcuts import render
from personas.models import Persona

def test(request):
    personas = Persona.objects.all()
    return render(request, "personas/test.html", {"personas": personas})
