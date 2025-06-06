from django.shortcuts import render
from personas.models import Persona
from personas.forms import PersonaForm
from django.shortcuts import render

def home(request):
    return render(request, "personas/test.html")  # O cambia "test.html" por la que quieras mostrar


# Vista principal que muestra lista de personas
def test(request):
    personas = Persona.objects.all()
    return render(request, "personas/test.html", {"personas": personas})

# Vista para crear una nueva persona
def crear_persona(request):
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PersonaForm()  # reinicia el formulario
    return render(request, "personas/personasCreate.html", {"form": form})

# Vista para búsqueda GET
def search_view(request):
    query = request.GET.get("q")
    return render(request, "personas/search.html", {"query": query})
