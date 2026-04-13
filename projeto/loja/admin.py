from django.contrib import admin
# Register your models here.
from .models import *
admin.site.register(Fabricante)
admin.site.register(Categoria)
admin.site.register(Produto)

# código para acessar: http://127.0.0.1:8080/admin
# código para rodar: python manage.py runserver 127.0.0.1:8080