from django.urls import path
from . import views
from .views import PersonaListView

urlpatterns = [
    path('', views.lista_personas, name='lista_personas'),
    path('crear/', views.crear_persona, name='crear_persona'),
    path('lista-cbv/', PersonaListView.as_view(), name='lista_cbv'),
]