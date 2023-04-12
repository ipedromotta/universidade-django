from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import Campo, Atividade

# Create your views here.
class CampoCreate(GroupRequiredMixin, CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-campos')
    login_url = reverse_lazy('nao-autenticado')
    group_required = u"Reitor"

class AtividadeCreate(LoginRequiredMixin, CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-atividades')
    login_url = reverse_lazy('login')
    
class CampoUpdate(GroupRequiredMixin, UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-campos')
    login_url = reverse_lazy('nao-autenticado')
    group_required = [u"Reitor", u"Grupo2"]
    
class AtividadeUpdate(LoginRequiredMixin, UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-atividades')
    login_url = reverse_lazy('login')
    
class CampoDelete(GroupRequiredMixin, DeleteView):
    model = Campo
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-campos')
    login_url = reverse_lazy('nao-autenticado')
    group_required = u"Reitor"
    
class AtividadeDelete(LoginRequiredMixin, DeleteView):
    model = Atividade
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-atividades')
    login_url = reverse_lazy('login')
    
class CampoList(LoginRequiredMixin, ListView):
    model = Campo
    template_name = 'campo.html'
    login_url = reverse_lazy('nao-autenticado')
    
class AtividadeList(LoginRequiredMixin, ListView):
    model = Atividade
    template_name = 'atividade.html'
    login_url = reverse_lazy('login')
