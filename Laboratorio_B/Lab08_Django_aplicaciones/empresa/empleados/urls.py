from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('email/', views.enviar_email, name='enviar_email'),
    path('pdf/', views.lista_empleados_pdf, name='pdf_empleados'),
]
