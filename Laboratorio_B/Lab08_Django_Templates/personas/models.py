from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    donador = models.BooleanField()

    def __str__(self):
        return self.nombre
