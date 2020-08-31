from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente

# Create your views here.

def cadastrar_cliente(request, template_name='cliente_form.html'):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_cliente')
    return render(request, template_name, {'form': form})

def listar_cliente(request, template_name='cliente_list.html'):
    query = request.GET.get("busca")
    if query:
        clientes = Cliente.objects.filter(telefone__icontains=query)
    else:
        clientes = Cliente.objects.all()
    return render(request, template_name, {'clientes': clientes})

def editar_cliente(request,pk, template_name='cliente_form.html'):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_cliente')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, template_name, {'form': form})

def remover_cliente(request,pk, template_name='cliente_delete.html'):
    cliente = Cliente.objects.get(pk = pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('listar_cliente')
    return render(request, template_name, {'cliente': cliente})
