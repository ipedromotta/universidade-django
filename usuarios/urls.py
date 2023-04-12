from django.urls import path
from django.contrib.auth import views as auth_views

from .views import nao_autenticado


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
            template_name='login.html'
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('nao-autenticado/', nao_autenticado, name='nao-autenticado'),
]
