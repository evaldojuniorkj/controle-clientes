from django.forms import ModelForm
from .models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['telefone', 'nome', 'logradouro', 'numero','bairro', 'ponto_referencia','data_cadastro']
