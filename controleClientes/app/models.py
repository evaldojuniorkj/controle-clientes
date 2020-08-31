from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime 
# Create your models here.

class Cliente(models.Model):
    telefone = models.CharField(max_length=50, null=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    ponto_referencia = models.TextField(null=True, blank=True)
    data_cadastro = models.DateTimeField(default=datetime.today, null=True, blank=True)

    def __str__(self):
        return self.nome

class Motorista(models.Model):
    nome = models.CharField(max_length=60)
    def __str__(self):
        return self.nome

class Servico(models.Model):
    descricao = models.CharField(max_length=60, null=False)
    valor = models.DecimalField(max_digits=5,decimal_places=2)
    def __str__(self):
        return self.descricao

class OrdemServiço(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)

class itemServiço(models.Model):
    servico = models.ForeignKey()
    ordem_servico
    quantidade
    valor