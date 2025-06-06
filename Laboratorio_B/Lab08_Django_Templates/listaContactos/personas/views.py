from django.shortcuts import render
from personas.models import Persona

def home(request):
    return render(request, "personas/test.html")


def test(request):
    personas = Persona.objects.all()
    return render(request, "personas/test.html", {"personas": personas})
