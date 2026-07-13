from django.shortcuts import render, redirect
from loja.models import Categoria

def categoria_view(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/categoria.html', {'categorias': categorias}, status=200)

def create_categoria_view(request):
    if request.method == 'POST':
        nome_categoria = request.POST.get('Categoria')
        if nome_categoria:
            obj = Categoria()
            obj.Categoria = nome_categoria
            obj.save()
        return redirect('/categoria')
    return render(request, 'categoria/categoria-create.html', status=200)

# FUNÇÃO DE DETALHES ADICIONADA AQUI:
def details_categoria_view(request, id=None):
    categoria = Categoria.objects.filter(id=id).first()
    return render(request, 'categoria/categoria-details.html', {'categoria': categoria}, status=200)

def edit_categoria_view(request, id=None):
    categoria = Categoria.objects.filter(id=id).first()
    if request.method == 'POST':
        nome_categoria = request.POST.get('Categoria')
        if categoria and nome_categoria:
            categoria.Categoria = nome_categoria
            categoria.save()
        return redirect('/categoria')
    return render(request, 'categoria/categoria-edit.html', {'categoria': categoria}, status=200)

def delete_categoria_view(request, id=None):
    categoria = Categoria.objects.filter(id=id).first()
    if request.method == 'POST':
        if categoria:
            categoria.delete()
        return redirect('/categoria')
    return render(request, 'categoria/categoria-delete.html', {'categoria': categoria}, status=200)