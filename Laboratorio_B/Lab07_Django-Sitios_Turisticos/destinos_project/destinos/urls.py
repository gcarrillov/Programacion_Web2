from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar/', views.agregar_destino, name='agregar_destino'),
    path('destinos/', views.destino_list, name='listar_destinos'),
    path('editar/<int:id>/', views.editar_destino, name='editar_destino'),
    path('eliminar/<int:id>/', views.eliminar_destino, name='eliminar_destino'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
