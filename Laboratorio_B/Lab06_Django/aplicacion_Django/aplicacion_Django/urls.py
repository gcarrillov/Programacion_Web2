from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def root_redirect(request):
    return redirect('lista_ventas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventas/', include('tienda.urls')),  # URLs de la app tienda
    path('', root_redirect),  # Redirige '/' a '/ventas/'
]
