from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from .forms import RegistroForm

class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('registrarUsu')

def cargarLogin(request):


    return render_to_response('usuario/index.html',context_instance = RequestContext(request))