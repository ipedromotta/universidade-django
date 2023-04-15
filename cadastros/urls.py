from django.urls import path

from .views import AvaliacaoCreate, AvaliacaoDelete, AvaliacaoList, AvaliacaoUpdate, CampoCreate, AtividadeCreate
from .views import CampoUpdate, AtividadeUpdate
from .views import CampoDelete, AtividadeDelete
from .views import CampoList, AtividadeList


urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('cadastrar/avaliacao/', AvaliacaoCreate.as_view(), name='cadastrar-avaliacao'),
    
    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>', AtividadeUpdate.as_view(), name='editar-atividade'),
    path('editar/avaliacao/<int:pk>', AvaliacaoUpdate.as_view(), name='editar-avaliacao'),
    
    path('deletar/campo/<int:pk>/', CampoDelete.as_view(), name='deletar-campo'),
    path('deletar/atividade/<int:pk>/', AtividadeDelete.as_view(), name='deletar-atividade'),
    path('deletar/avaliacao/<int:pk>/', AvaliacaoDelete.as_view(), name='deletar-avaliacao'),
    
    path('listar/campos/', CampoList.as_view(), name='listar-campos'),
    path('listar/atividades/', AtividadeList.as_view(), name='listar-atividades'),
    path('listar/avaliacoes/', AvaliacaoList.as_view(), name='listar-avaliacoes'),
    
]
