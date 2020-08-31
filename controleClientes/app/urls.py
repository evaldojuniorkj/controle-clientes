from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('listar_cliente/', views.listar_cliente, name='listar_cliente'),
    path('editar_cliente/<int:pk>', views.editar_cliente, name='editar_cliente'),
    path('remover_cliente/<int:pk>', views.remover_cliente, name='remover_cliente'),
]