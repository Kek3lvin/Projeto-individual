from django.urls import path
from loja.views.FabricanteView import (
    fabricante_view,
    create_fabricante_view,
    details_fabricante_view,
    edit_fabricante_view,
    delete_fabricante_view
)

urlpatterns = [
    path('', fabricante_view, name='fabricante'),
    path('create', create_fabricante_view, name='fabricante-create'),
    path('details/<int:id>', details_fabricante_view, name='fabricante-details'),
    path('edit/<int:id>', edit_fabricante_view, name='fabricante-edit'),
    path('delete/<int:id>', delete_fabricante_view, name='fabricante-delete'),
]