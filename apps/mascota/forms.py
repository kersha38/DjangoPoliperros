from django import forms

from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model=Mascota

        fields=['nombre',
                'sexo',
                'edad_aproximada',
                'color',
                'fecha_ingreso',
                'estado_Actual',
                'persona']

        labels = {'nombre':'Nombre',
                  'sexo':'Sexo',
                  'edad_aproximada':'Edad',
                  'color':'Color',
                  'fecha_ingreso':'Fecha Registro',
                  'estado_Actual':'Estado',
                  'persona':'Adoptante'}

        sexo=[]
        sexo.append('Masculino')
        sexo.append('Femenino')
        widgets = {'nombre':forms.TextInput(attrs={'class':'form-control'}),
                   'sexo':forms.TextInput(),
                   'edad_aproximada':forms.TextInput(attrs={'class':'form-control'}),
                   'color':forms.TextInput(attrs={'class':'form-control'}),
                   'fecha_ingreso':forms.SelectDateWidget(),
                   'estado_Actual':forms.TextInput(attrs={'class':'form-control'}),
                   'persona':forms.Select(attrs={'class':'form-control'})}
