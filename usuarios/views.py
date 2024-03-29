from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth.models import Group
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import CreateView, UpdateView

from .forms import UsuarioForm
from .models import Perfil


# Create your views here.
class UsuarioCreate(CreateView):
    template_name = 'form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Docente")
        
        url = super().form_valid(form)
        
        self.object.groups.add(grupo)
        self.object.save()
        
        Perfil.objects.create(usuario=self.object)
        
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Crie a sua conta'
        
        return context

def nao_autenticado(request):
    return render(request, 'autenticacao.html')

class PerfilUpdate(UpdateView):
    template_name = 'form.html'
    model = Perfil
    fields = ['nome_completo', 'cpf', 'telefone']
    success_url = reverse_lazy('inicio')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Meus dados pessoais"
        context['botao'] = "Atualizar"
        
        return context
    
class SenhaUpdate(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('inicio')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Atualizar senha'
        context['botao'] = 'Atualizar'
        
        return context
    