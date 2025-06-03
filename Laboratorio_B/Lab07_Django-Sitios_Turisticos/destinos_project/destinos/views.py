from django.shortcuts import render, redirect
from .models import DestinosTuristicos
from .forms import DestinoForm, RegistroForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def destino_list(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'destinos/destino_list.html', {'destinos': destinos})

@login_required
def editar_destino(request, id):
    destino = get_object_or_404(DestinosTuristicos, id=id)
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('listar_destinos')
    else:
        form = DestinoForm(instance=destino)
    return render(request, 'destinos/destino_form.html', {'form': form})

@login_required
def eliminar_destino(request, id):
    destino = get_object_or_404(DestinosTuristicos, id=id)
    if request.method == 'POST':
        destino.delete()
        return redirect('listar_destinos')
    return render(request, 'destinos/eliminar_confirmar.html', {'destino': destino})


def home(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'destinos/home.html', {'destinos': destinos})

def agregar_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DestinoForm()
    return render(request, 'destinos/destino_form.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'destinos/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'destinos/register.html', {'form': form})
