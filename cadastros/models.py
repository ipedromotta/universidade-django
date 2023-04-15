from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    
    def __str__(self) -> str:
        return f"{self.nome} - {self.descricao}"
    
class Atividade(models.Model):
    numero = models.IntegerField(verbose_name="Número")
    descricao = models.CharField(max_length=150, verbose_name="Descricão")
    pontos = models.DecimalField(decimal_places=1, max_digits=4)
    detalhes = models.CharField(max_length=100)
    
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.numero} - {self.descricao} ({self.campo.nome})"
    
class Avaliacao(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    arquivo = models.FileField(upload_to='pdf/')
    
    def __str__(self) -> str:
        return f'[{self.pk}] {self.usuario} - {self.atividade}/{self.atividade.campo}'
    
    class Meta:
        verbose_name_plural = "Avaliações"
        verbose_name = "Avaliação"
    