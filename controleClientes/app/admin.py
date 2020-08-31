from django.contrib import admin
from .models import Cliente, Motorista, Servico
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Motorista)
admin.site.register(Servico)