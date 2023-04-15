from django.urls import path
from .views import PaginaInicial, SobreView, AjudaView


urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('ajuda/', AjudaView.as_view(), name='ajuda'),
]
