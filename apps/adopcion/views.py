from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView,DeleteView, UpdateView
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

class SolicitudUpdate(UpdateView):
	model = Solicitud
	second_model = Persona
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('solicitudList')


	def get_context_data(self, **kwargs):
	    context = super(SolicitudUpdate, self).get_context_data(**kwargs)
	    pk = self.kwargs.get('pk', 0)
	    solicitud = self.model.objects.get(id=pk)
	    persona = self.second_model.objects.get(id=solicitud.persona_id)
	    if 'form' not in context:
	    	context['form'] = self.form_class()
	    if 'formPers' not in context:
	    	context['formPers'] = self.second_form_class(instance=persona)
	    context['id'] = pk
	    return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_solicitud = kwargs['pk']
		solicitud = self.model.objects.get(id=id_solicitud)
		persona = self.second_model.objects.get(id=solicitud.persona_id)
		form = self.form_class(request.POST, instance=solicitud)
		formPers = self.second_form_class(request.POST, instance=persona)
		if form.is_valid() and formPers.is_valid():
			form.save()
			formPers.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())

class solicitudDelete(DeleteView):
    model = Solicitud
    form_class=SolicitudForm
    template_name = 'adopcion/solicitud_delete.html'
    success_url = reverse_lazy('solicitudList')