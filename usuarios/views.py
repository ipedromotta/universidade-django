from django.shortcuts import render

# Create your views here.
def nao_autenticado(request):
    return render(request, 'autenticacao.html')
