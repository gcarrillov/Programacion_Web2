from django import forms
from .models import DestinosTuristicos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DestinoForm(forms.ModelForm):
    class Meta:
        model = DestinosTuristicos
        fields = '__all__'

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
