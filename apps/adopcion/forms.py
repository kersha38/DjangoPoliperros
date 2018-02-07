from django import forms

from apps.adopcion.models import Persona, Solicitud

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellido',
            'cedula',
            'edad',
            'telefono',
            'email',
            'domicilio',
            'personaEPN',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'cedula': 'Cedula',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Correo electrónico',
            'domicilio': 'Dirección domiciliaria',
            'personaEPN': 'Usted pertenece a la E.P:N.?',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'cedula': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'personaEPN': forms.NullBooleanSelect(),
        }

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'numero_mascotas',
            'razones',
        ]
        labels = {
            'numero_mascotas': 'Número de mascotas para adopción',
            'razones': 'Razones de su adopción',
        }
        widgets = {
            'numero_mascotas': forms.NumberInput(attrs={'class':'form-control'}),
            'razones': forms.TextInput(attrs={'class':'form-control'}),
        }