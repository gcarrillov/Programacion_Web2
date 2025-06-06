from django.shortcuts import render
from personas.models import Persona

def test(request):
    persona = Persona.objects.first()
    return render(request, "personas/test.html", {"persona": persona})
