from django.db import models

# Create your models here.
class formularioContacto(models.Model):
    nombre=models.CharField(max_length=15)
    email = models.EmailField()
    asunto= models.CharField(max_length=15)
    mensaje= models.CharField(max_length=13)
