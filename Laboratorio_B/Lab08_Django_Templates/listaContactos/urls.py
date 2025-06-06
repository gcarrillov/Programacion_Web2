from django.contrib import admin
from django.urls import path
from personas import views  # importa tus vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('persona/', views.test, name='persona'),  # ruta para test.html
    path('personas/crear/', views.crear_persona, name='crear_persona'),
    path('personas/buscar/', views.search_view, name='buscar_persona'),
]
