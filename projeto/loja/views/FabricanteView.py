from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Fabricante
from loja.forms.FabricanteForm import FabricanteForm

# Listagem de Fabricantes
def fabricante_view(request):
    fabricantes = Fabricante.objects.all()
    return render(request, 'fabricante/fabricante.html', {'fabricantes': fabricantes}, status=200)

# Criar Fabricante
def create_fabricante_view(request):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fabricante')
    else:
        form = FabricanteForm()
    
    return render(request, 'fabricante/fabricante-create.html', {'form': form}, status=200)

# Detalhes do Fabricante
def details_fabricante_view(request, id=None):
    fabricante = get_object_or_404(Fabricante, id=id)
    return render(request, 'fabricante/fabricante-details.html', {'fabricante': fabricante}, status=200)

# Editar Fabricante
def edit_fabricante_view(request, id=None):
    fabricante = get_object_or_404(Fabricante, id=id)
    if request.method == 'POST':
        form = FabricanteForm(request.POST, instance=fabricante)
        if form.is_valid():
            form.save()
            return redirect('fabricante')
    else:
        form = FabricanteForm(instance=fabricante)
        
    return render(request, 'fabricante/fabricante-edit.html', {'form': form, 'fabricante': fabricante}, status=200)

# Excluir Fabricante
def delete_fabricante_view(request, id=None):
    fabricante = get_object_or_404(Fabricante, id=id)
    if request.method == 'POST':
        fabricante.delete()
        return redirect('fabricante')
        
    return render(request, 'fabricante/fabricante-delete.html', {'fabricante': fabricante}, status=200)