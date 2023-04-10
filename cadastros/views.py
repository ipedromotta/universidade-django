from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Campo, Atividade

# Create your views here.
class CampoCreate(CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-campos')

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-atividades')
    
class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-campos')
    
class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-atividades')
    
class CampoDelete(DeleteView):
    model = Campo
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-campos')
    
class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-atividades')
    
class CampoList(ListView):
    model = Campo
    template_name = 'campo.html'
    
class AtividadeList(ListView):
    model = Atividade
    template_name = 'atividade.html'
