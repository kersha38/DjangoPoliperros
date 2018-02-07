from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    cedula=models.CharField(max_length=13)
    edad=models.IntegerField()
    telefono=models.CharField(max_length=15)
    email=models.CharField(max_length=30)
    domicilio=models.CharField(max_length=30)
    personaEPN=models.BooleanField()

    def __str__(self):
        return self.nombre+' '+self.apellido

class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()

    def __str__(self):
        return self.persona+' '+self.numero_mascotas+' '+self.razones