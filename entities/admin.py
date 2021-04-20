from django.contrib import admin
from entities.models import *

# Register your models here.
admin.site.register(Consulta)
admin.site.register(EstadoConsulta)
admin.site.register(TipoProblema)
admin.site.register(TipoSolicitante)
admin.site.register(Solicitante)
admin.site.register(Sector)

