from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404

from .models import Avaliacao, Campo, Atividade


# Create your views here.
class CampoCreate(GroupRequiredMixin, CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-campos')
    login_url = reverse_lazy('nao-autenticado')
    group_required = u"Reitor"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Cadastro de campos"
        
        return context

class AtividadeCreate(LoginRequiredMixin, CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-atividades')
    login_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Cadastro de atividades"
        
        return context
    
class AvaliacaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Avaliacao
    fields = ['atividade', 'arquivo']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-avaliacoes')
        
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['atividade'].queryset = Atividade.objects.filter(usuario=self.request.user)
        
        return form
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Cadastro de avaliações"
        context['upload'] = "multipart/form-data"
        
        return context
    
class CampoUpdate(GroupRequiredMixin, UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-campos')
    login_url = reverse_lazy('nao-autenticado')
    group_required = [u"Reitor", u"Grupo2"]
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Editar Campo"
        context['botao'] = "Salvar"
        
        return context
    
class AtividadeUpdate(LoginRequiredMixin, UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-atividades')
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Atividade, pk=self.kwargs['pk'], usuario=self.request.user)
        
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Editar Atividade"
        context['botao'] = "Salvar"
        
        return context
    
class AvaliacaoUpdate(GroupRequiredMixin, UpdateView):
    model = Avaliacao
    fields = ['atividade', 'arquivo']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-avaliacoes')
    login_url = reverse_lazy('nao-autenticado')
    group_required = u"Reitor"
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Avaliacao, pk=self.kwargs['pk'])
        
        return self.object
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        atividade = Atividade.objects.get(pk=self.kwargs['pk'])
        form.fields['atividade'].queryset = Atividade.objects.filter(usuario=atividade.usuario)
        
        return form
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Editar Avaliação"
        context['botao'] = "Salvar"
        context['upload'] = "multipart/form-data"
        
        return context
    
class CampoDelete(GroupRequiredMixin, DeleteView):
    model = Campo
    template_name = 'form.html'
    success_url = reverse_lazy('listar-campos')
    login_url = reverse_lazy('nao-autenticado')
    group_required = u"Reitor"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Excluir campo"
        context['subtitulo'] = "Confirme para excluir o campo definitivamente"
        context['botao'] = "Excluir"
        context['estilo_botao'] = "btn-danger"
        context['tag_exclusao'] = True
        
        return context
    
class AtividadeDelete(LoginRequiredMixin, DeleteView):
    model = Atividade
    template_name = 'form.html'
    success_url = reverse_lazy('listar-atividades')
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Atividade, pk=self.kwargs['pk'], usuario=self.request.user)
        
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Excluir atividade"
        context['subtitulo'] = "Confirme para excluir a atividade definitivamente"
        context['botao'] = "Excluir"
        context['estilo_botao'] = "btn-danger"
        context['tag_exclusao'] = True
        
        return context
    
class AvaliacaoDelete(GroupRequiredMixin, DeleteView):
    model = Avaliacao
    template_name = 'form.html'
    success_url = reverse_lazy('listar-avaliacoes')
    login_url = reverse_lazy('nao-autenticado')
    group_required = u"Reitor"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Excluir avaliação"
        context['subtitulo'] = "Confirme para excluir a avaliação definitivamente"
        context['botao'] = "Excluir"
        context['estilo_botao'] = "btn-danger"
        context['tag_exclusao'] = True
        
        return context
    
class CampoList(LoginRequiredMixin, ListView):
    model = Campo
    template_name = 'campo.html'
    login_url = reverse_lazy('nao-autenticado')
    
class AtividadeList(LoginRequiredMixin, ListView):
    model = Atividade
    template_name = 'atividade.html'
    login_url = reverse_lazy('login')
    # paginate_by = 1 # Limita o numero de registros exibidos na tela, dentro do HTML tem a paginação e validação. É mais rápido que o DataTable se tiver uma quantidade de registros gigantesca
    
    def get_queryset(self):
        # Desabilitado pois já estou utilizando DataTable, o codigo comentado filtra as paginas de acordo com a pesquisa do usuario
        # input_usuario = self.request.GET.get('detalhes')
        # if input_usuario:
        #     self.object_list = Atividade.objects.filter(Q(usuario=self.request.user) & Q(detalhes__icontains=input_usuario))
        # else:
        #     self.object_list = Atividade.objects.filter(usuario=self.request.user)
            
        self.object_list = Atividade.objects.filter(usuario=self.request.user)
        
        return self.object_list

class AvaliacaoList(LoginRequiredMixin, ListView):
    model = Avaliacao
    template_name = 'avaliacao.html'
    login_url = reverse_lazy('nao-autenticado')
    
    def get_queryset(self, queryset=None):
        self.object_list = Avaliacao.objects.filter(usuario=self.request.user)
        
        if self.request.user.groups.filter(name='Reitor').exists():
            self.object_list = Avaliacao.objects.all()
        
        return self.object_list
