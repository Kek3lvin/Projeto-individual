from django.contrib import admin

# Register your models here.
from .models import *

class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao','preco', 'categoria',)
    search_fields = ('Produto',)
    fields = ('Produto', 'destaque', 'promocao','msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'

admin.site.register(Fabricante,FabricanteAdmin)
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)


# código para acessar: http://127.0.0.1:8080/admin
# código para rodar: python manage.py runserver 127.0.0.1:8080
# código para ativar os scripts: venv\Scripts\activate