from django.db import models,migrations

# Create your models here.
class Grafico(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.nombre)
