from django.urls import path
from loja.views.CategoriaView import *

urlpatterns = [
    path('', categoria_view, name='categoria'),
    path('create', create_categoria_view, name='categoria-create'),
    path('details/<int:id>', details_categoria_view, name='categoria-details'), # Adicione esta linha!
    path('edit/<int:id>', edit_categoria_view, name='categoria-edit'),
    path('delete/<int:id>', delete_categoria_view, name='categoria-delete'),
]