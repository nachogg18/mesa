from django.urls import path
from .views import ConsultaAutenticadaCreateView, ConsultaNoAutenticadaCreateView, ConsultaListView

urlpatterns = [
    path('', ConsultaListView.as_view(), name='home'),
    path('create/', ConsultaAutenticadaCreateView.as_view(), name='create'),
    path('createNoAuth/', ConsultaNoAutenticadaCreateView.as_view(), name='createNoAuth'),
]