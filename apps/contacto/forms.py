from django import forms
from apps.contacto.models import formularioContacto

class contactoForm(forms.ModelForm):
    class Meta:
        model = formularioContacto

        fields = [
            'nombre',
            'email',
            'asunto',
            'mensaje',
        ]

        labels = {
            'nombre': 'Nombre',
            'email':'Email',
            'asunto':'Asunto',
            'mensaje':'Mensaje',

                  }

        widgets = {

            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje':forms.Textarea(attrs={'class':'form-control'}),
            }

'''

class formularioContacto(forms.Form):
    correo = forms.EmailField()
    mensaje = forms.CharField()
'''