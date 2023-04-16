from django.urls import path
from django.contrib.auth import views as auth_views

from .views import nao_autenticado
from .views import UsuarioCreate, PerfilUpdate, SenhaUpdate


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
            template_name='login.html'
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('nao-autenticado/', nao_autenticado, name='nao-autenticado'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    path('atualizar-dados/', PerfilUpdate.as_view(), name='atualizar-dados'),
    path('atualizar-senha/', SenhaUpdate.as_view(), name='atualizar-senha'),
]
