from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm
from django.shortcuts import redirect

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/lista.html', {'personas': personas})

def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            # Guardar en la base de datos (lo haremos luego)
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'personas/formulario.html', {'form': form})