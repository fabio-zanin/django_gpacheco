from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClienteForm
from .models import Cliente


@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'list.html', {'clientes': clientes})


@login_required
def cliente_new(request):
    form = ClienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('clientes:cliente_list')    
    return render(request, 'new.html', {'form': form})


@login_required
def cliente_update(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('clientes:cliente_list')
    return render(request, 'new.html', {'form': form})


@login_required
def cliente_delete(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes:cliente_list')
    return render(request, 'cliente_delete_confirm.html', {'cliente': cliente})
