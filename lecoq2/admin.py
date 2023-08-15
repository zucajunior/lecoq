from django.contrib import admin
from .models import TabelaNutricionalProduto, ItemTabelaNutricional, ItemIngrediente, Ingrediente,\
    Produto, Cliente, Pedido, ItensPedido

admin.site.register(TabelaNutricionalProduto)
admin.site.register(ItemTabelaNutricional)
admin.site.register(Ingrediente)
admin.site.register(ItemIngrediente)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(ItensPedido)
