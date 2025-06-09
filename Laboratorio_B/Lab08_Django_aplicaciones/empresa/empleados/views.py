from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleado
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import send_mail
from django.http import HttpResponse

def enviar_email(request):
    send_mail(
        subject='Reporte de empleados',
        message='Este es un correo de prueba con Django.',
        from_email='from@example.com',  # opcional si ya tienes DEFAULT_FROM_EMAIL
        recipient_list=['to@example.com'],  # puede ser tu correo de pruebas
        fail_silently=False,
    )
    return HttpResponse("Correo enviado correctamente")

def lista_empleados_pdf(request):
    empleados = Empleado.objects.all()
    template = get_template('empleados/pdf_empleados.html')
    html = template.render({'empleados': empleados})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="empleados.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response