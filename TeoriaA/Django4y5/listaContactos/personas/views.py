from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm
from django.shortcuts import redirect
from django.views.generic import ListView

class PersonaListView(ListView):
    model = Persona
    template_name = 'personas/lista_cbv.html'
    context_object_name = 'personas'
def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/lista.html', {'personas': personas})

from .models import Persona

def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            # Guardar manualmente en la BD
            Persona.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email']
            )
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'personas/formulario.html', {'form': form})