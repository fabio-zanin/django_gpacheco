from django.shortcuts import redirect, render

from .forms import ClienteForm
from .models import Cliente


def home(request):    
    return render(request, 'clientes.html')

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'list.html', {'clientes': clientes})


def cliente_new(request):
    form = ClienteForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
        return redirect('clientes:cliente_list')    
    return render(request, 'new.html', {'form': form})
