from django.contrib import admin
from apps.mascota.models import Mascota, Visita_Medica, Medicina
from apps.adopcion.models import Persona

# Register your models here.
admin.site.register(Mascota)
admin.site.register(Visita_Medica)
admin.site.register(Persona)
admin.site.register(Medicina)
