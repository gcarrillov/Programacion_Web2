from django.db import models

# Relación uno a muchos: Departamento -> Empleado
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# Relación muchos a muchos: Empleado <-> Proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    empleados = models.ManyToManyField(Empleado, related_name='proyectos')

    def __str__(self):
        return self.nombre
