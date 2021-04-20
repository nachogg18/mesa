from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import ConsultaCreateForm
from django.views.generic import ListView, CreateView

# Create your views here.
from .models import Consulta, Solicitante, EstadoConsulta
from django.contrib.auth.decorators import login_required

'''
def agregarConsulta(request):
    # We create an empty form
    form = ConsultaNoAutenticadaForm()

    # We check if the form has been sent
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = ConsultaNoAutenticadaForm(data=request.POST)

        if form.is_valid():
            # We save the form but without confirming it,
            # so we will get an instance to handle it
            instancia = form.save(commit=False)
            instancia.save()

            #send_async_html_message.delay(instancia.id)
            # After saving we redirect to the list
            return redirect('/')

        # If we reach the end we render the form
    return render(request, "mesa/home.html", {'form': form})
'''

class ConsultaListView(LoginRequiredMixin, ListView):
    model = Consulta


class ConsultaAutenticadaCreateView(CreateView):
    model = Consulta
    fields = ['asuntoConsulta', 'descripcionConsulta', 'tipoProblema']
    success_url = '/'

    def form_valid(self, form):
        form.instance.estadoConsulta = EstadoConsulta.objects.get(nombreEstadoConsulta='PENDIENTE')
        return super().form_valid(form)


class ConsultaNoAutenticadaCreateView(CreateView):
    model = Consulta
    fields = ['asuntoConsulta', 'descripcionConsulta', 'tipoProblema', 'nombreSolicitante', 'apellidoSolicitante', 'emailSolicitante' ]
    success_url = '/'

    def form_valid(self, form):
        form.instance.estadoConsulta = EstadoConsulta.objects.get(nombreEstadoConsulta='PENDIENTE')
        return super().form_valid(form)



