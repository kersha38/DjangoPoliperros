from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.mascota.forms import MascotaForm ,VisitaMedicaForm
from apps.mascota.models import Mascota,Visita_Medica
# Create your views here.

def index(request):
    return render(request,'mascota/index.html')

def mascota_crear(request):
    if request.method=='POST':
        form=MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascotaListar')
    else:
        form=MascotaForm()
    return render(request,'mascota/mascota_form.html',{'form':form})

def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas': mascota}
    return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascotaListar')
    return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascotaListar')
    return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})

class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascotaListar') #es resolver de paginas, si fue bien  o no

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascotaListar')

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascotaListar')

def visita_crear(request):
    if request.method=='POST':
        form= VisitaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitaListar')
    else:
        form=VisitaMedicaForm()
    return render(request,'mascota/visita_medica.html',{'form':form})

class VisitaCreate(CreateView):
    model = Visita_Medica
    form_class = VisitaMedicaForm
    template_name = 'mascota/visita_medica.html'
    success_url = reverse_lazy('mascotaListar') #es resolver de paginas, si fue bien  o no


def visita_list(request,id_visita):
    visita = Visita_Medica.objects.filter(mascota_id=id_visita)
    contexto = {'object_list': visita}
    return render(request, 'mascota/visita_lista.html', contexto)

class VisitaUpdate(UpdateView):
    model = Visita_Medica
    form_class = VisitaMedicaForm
    template_name = 'mascota/visita_medica.html'
    success_url = reverse_lazy('mascotaListar')


class VisitaDelete(DeleteView):
    model = Visita_Medica
    template_name = 'mascota/visita_delete.html'
    success_url = reverse_lazy('mascotaListar')

def visitamedica_crear(request):
    if request.method=='POST':
        form=VisitaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascotaListar')
    else:
        form=VisitaMedicaForm()
    return render(request,'mascota/visita_medica.html',{'form':form})