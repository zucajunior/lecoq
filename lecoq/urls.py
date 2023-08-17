from django.contrib import admin
from django.urls import path
from lecoq2 import views

urlpatterns = [
   path('', views.home, name='home'),  # Página inicial

    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),

    path('cliente/<int:cliente_id>/', views.detalhes_cliente, name='detalhes_cliente'),
    path('cliente/<int:cliente_id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('cliente/<int:cliente_id>/excluir/', views.excluir_cliente, name='excluir_cliente'),


    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produto/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('produto/<int:produto_id>/excluir/', views.excluir_produto, name='excluir_produto'),
    path('produto/<int:produto_id>/editar/', views.editar_produto, name='editar_produto'),

    path('ingredientes/', views.listar_ingredientes, name='listar_ingredientes'),
    path('ingredientes/cadastrar/', views.cadastrar_ingrediente, name='cadastrar_ingrediente'),

    path('itens_nutricionais/', views.listar_itens_nutricionais, name='listar_itens_nutricionais'),
    path('itens_nutricionais/cadastrar/', views.cadastrar_item_nutricional, name='cadastrar_item_nutricional'),

    path('tabelas_nutricionais/', views.listar_tabelas_nutricionais, name='listar_tabelas_nutricionais'),
    path('tabelas_nutricionais/cadastrar/', views.cadastrar_tabela_nutricional, name='cadastrar_tabela_nutricional'),

    path('pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('pedidos/cadastrar/', views.cadastrar_pedido, name='cadastrar_pedido'),
    path('itens_pedido/cadastrar/<int:pedido_id>/', views.cadastrar_item_pedido, name='cadastrar_item_pedido'),
    path('pedidosaberto/', views.pedidos_aberto, name='pedidos_aberto'),
    path('itens_pedido/', views.listar_itens_pedido, name='listar_itens_pedido'),

    path('editar_pedido/<int:codigo>/', views.editar_pedido, name='editar_pedido'),
    path('excluir_pedido/<int:codigo>/', views.excluir_pedido, name='excluir_pedido'),
    path('get_preco/<int:produto_id>/', views.get_preco, name='get_preco'),

    path('tabelas_nutricionais_produtos/cadastrar/', views.cadastrar_tabela_nutricional_produto,
         name='cadastrar_tabela_nutricional_produto'),
    path('tabelas_nutricionais_produtos/', views.listar_tabelas_nutricionais_produto,
         name='listar_tabelas_nutricionais_produto'),
    path('listar_tabelas_nutricionais_produto/', views.listar_tabelas_nutricionais_produto,
         name='listar_tabelas_nutricionais_produto'),

    path('pedido/<int:pedido_id>/', views.detalhes_pedido,
         name='detalhes_pedido'),
    path('pedido/<int:pedido_id>/item/<int:cod_prod>/editar/', views.editar_item_pedido,
         name='editar_item_pedido'),
    path('pedido/<int:pedido_id>/item/<int:cod_prod>/excluir/', views.excluir_item_pedido,
         name='excluir_item_pedido'),
    path('pedido/<int:pedido_id>/imprimir/', views.imprimir_pedido,
         name='imprimir_pedido'),
    path('relatorio/', views.relatorio_resumo, name='relatorio_resumo'),




    path('admin/', admin.site.urls),
]
