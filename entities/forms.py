from .models import Consulta
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

'''
class ConsultaAutenticadaForm(ModelForm):
     class Meta:
         model = Consulta
         fields = ['asuntoConsulta', 'descripcionConsulta', 'tipoProblema']


class ConsultaNoAutenticadaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['asuntoConsulta', 'descripcionConsulta', 'tipoProblema', 'nombreSolicitante', 'apellidoSolitante', 'emailSolicitante']
        labels = {
            'asuntoConsulta': 'Asunto',
            'descripcionConsulta': 'Descripcion' ,
            'tipoProblema': 'Tipo de Problema',
            'nombreSolicitante': 'Nombre del Solicitante',
            'apellidoSolitante': 'Apellido del Solicitante',
            'emailSolicitante': 'Email del Solicitante'
        }
'''

class ConsultaCreateForm(ModelForm):
    class Meta:
        model : Consulta