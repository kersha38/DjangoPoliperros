from django.db import models
from apps.adopcion.models import Persona

class Medicina(models.Model):
    medicina=models.CharField(max_length=20)

    def __str__(self):
        return  str(self.medicina)

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    color= models.CharField(max_length=20)
    fecha_ingreso= models.DateField()
    estado_Actual = models.CharField(max_length=15)
    persona=models.ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)

class Visita_Medica(models.Model):
    mascota=models.ForeignKey(Mascota,null=True,blank=True,on_delete=models.CASCADE)
    fecha=models.DateField()
    diagnostico=models.TextField()
    peso=models.FloatField()
    medicina=models.ForeignKey(Medicina,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(str(self.fecha)+' M: '+self.medicina)