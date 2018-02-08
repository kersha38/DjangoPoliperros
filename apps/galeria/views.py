from django.shortcuts import render
from django.http import HttpResponse

from apps.galeria.models import Grafico
# Create your views here.

def grafico (request):
    return render(request, 'galeria/extras.html')


#class grafico():
 #   template_name = 'galeria/extras.html'



