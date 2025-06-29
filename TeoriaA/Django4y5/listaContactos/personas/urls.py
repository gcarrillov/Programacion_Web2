from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_personas, name='lista_personas'),
    path('crear/', views.crear_persona, name='crear_persona'),
]