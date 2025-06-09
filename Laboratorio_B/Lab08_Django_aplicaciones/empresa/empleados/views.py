from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleado
from django.template.loader import get_template
from xhtml2pdf import pisa

def lista_empleados_pdf(request):
    empleados = Empleado.objects.all()
    template = get_template('empleados/pdf_empleados.html')
    html = template.render({'empleados': empleados})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="empleados.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response
