from apps.contacto.forms import contactoForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.contacto.models import formularioContacto


# Create your views here.

def contacto_view(request):
	if request.method == 'POST':
		form = contactoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('#')
	else:
		form = contactoForm()
	return render(request, 'contacto/contacto.html', {'form':form})






















"""
def gracias(request):
    html='<html><body>"Gracias por enviarnos su comentario.."</body></html>'
    return HttpResponse"""

'''
def contactoemail(request):
    if request.method =='post':
        formulario =formularioContacto(request.REST)
        if formulario.is_valid():
            asunto = "Comentario"
            mensaje= formulario.cleaned_data['mensaje']
            mail = EmailMessage(asunto,mensaje,to=['villacis.andrean12@gmail.com'])
            mail.send()
            return  HttpResponseRedirect('/')
        else:
            formulario=formularioContacto()

        return render_to_response('contacto.html',{'formulario':formulario},
                                                   context_instance=RequestContext(request))


'''


