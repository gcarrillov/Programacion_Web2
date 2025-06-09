from django.urls import path
from . import views

urlpatterns = [
    path('email/', views.enviar_email, name='enviar_email'),
]
