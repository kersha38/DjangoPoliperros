from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, SolicitudForm

def index(request):
    return HttpResponse('Page: Adopciones')

class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list.html'

class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('solicitudList')

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'formPers' not in context:
            context['formPers'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        formPers = self.second_form_class(request.POST)
        if form.is_valid() and formPers.is_valid():
            solicitud = form.save(commit=False)# false hasta que no guarde 2do formulario
            solicitud.persona = formPers.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, formPers=formPers))