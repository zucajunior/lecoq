from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Produto, ItemIngrediente, ItemTabelaNutricional, \
    TabelaNutricionalProduto, Ingrediente, ItensPedido, Pedido
from .forms import ClienteForm, ProdutoForm, PedidoForm, ItemTabelaNutricionalForm, \
    ItemIngredienteForm, TabelaNutricionalProdutoForm, ItemPedidoForm
from django.http import HttpResponse
from .utils import gerar_pdf_pedido  # Importe a função para gerar o PDF
from django.http import JsonResponse


def home(request):
    return render(request, 'index.html')




def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'editar_cliente.html', {'form': form})

def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')

    return render(request, 'excluir_cliente.html', {'cliente': cliente})

def detalhes_cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    return render(request, 'detalhes_cliente.html', {'cliente': cliente})

def listar_clientes(request):
    clientes = Cliente.objects.all().order_by('nome')
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cadastro_cliente.html', {'form': form})





""" P R O D U T O S   ***   P R O D U T O S   ***   P R O D U T O S   ***   """


def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')

    return render(request, 'excluir_produto.html', {'produto': produto})

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'editar_produto.html', {'form': form})

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')  # Redirecionar para a lista de produtos após o cadastro
    else:
        form = ProdutoForm()
    return render(request, 'cadastrar_produto.html', {'form': form})

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'detalhes_produto.html', {'produto': produto})

def listar_produtos(request):
    produtos = Produto.objects.all().order_by('nome')
    return render(request, 'listar_produtos.html', {'produtos': produtos})






def listar_ingredientes(request):
    ingredientes = ItemIngrediente.objects.all().order_by('descricao')
    return render(request, 'listar_ingredientes.html', {'ingredientes': ingredientes})

def listar_nutri(request):
    tabelas_nutricionais = ItemTabelaNutricional.objects.all()
    return render(request, 'listar_nutri.html', {'tabelas_nutricionais': tabelas_nutricionais})





""" P E D I D O S   ***   P E D I D O S   ***   P E D I D O S   ***   """

def imprimir_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)

    # Gera o PDF do pedido usando a função do utils
    pdf_file = gerar_pdf_pedido(pedido)

    # Define o cabeçalho do response para PDF
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="pedido_{pedido_id}.pdf"'

    return response

def pedidos_aberto(request):
    pedidos = Pedido.objects.filter(faturado=False)
    context = {'pedidos': pedidos}
    return render(request, 'listar_pedidos.html', context)

def listar_pedidos(request):
    faturado = request.GET.get('faturado')  # Obtém o valor do parâmetro 'faturado'

    if faturado == 'True':
        pedidos = Pedido.objects.order_by('-data_criacao').filter(faturado=True)
    elif faturado == 'False':
        pedidos = Pedido.objects.order_by('-data_criacao').filter(faturado=False)
    else:
        pedidos = Pedido.objects.order_by('-data_criacao').all()

    return render(request, 'listar_pedidos.html', {'pedidos': pedidos})

def detalhes_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    itens_pedido = ItensPedido.objects.filter(cod_pedido=pedido)
    return render(request, 'detalhes_pedido.html', {'pedido': pedido, 'itens_pedido': itens_pedido})

def editar_item_pedido(request, pedido_id, cod_prod):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    item = get_object_or_404(ItensPedido, cod_pedido=pedido, cod_prod=cod_prod)

    if request.method == 'POST':
        form = ItemPedidoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('detalhes_pedido', pedido_id=pedido.pk)
    else:
        form = ItemPedidoForm(instance=item)

    return render(request, 'editar_item_pedido.html', {'form': form, 'pedido': pedido, 'item': item})

def excluir_item_pedido(request, pedido_id, cod_prod):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    item = get_object_or_404(ItensPedido, cod_pedido=pedido, cod_prod=cod_prod)

    if request.method == 'POST':
        item.delete()
        return redirect('detalhes_pedido', pedido_id=pedido.pk)

    return render(request, 'excluir_item_pedido.html', {'pedido': pedido, 'item': item})

def editar_pedido(request, codigo):
    pedido = get_object_or_404(Pedido, codigo=codigo)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'editar_pedido.html', {'form': form})

def excluir_pedido(request, codigo):
    pedido = get_object_or_404(Pedido, codigo=codigo)
    if request.method == 'POST':
        pedido.delete()
        return redirect('listar_pedidos')
    return render(request, 'excluir_pedido.html', {'pedido': pedido})

def cadastrar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            return redirect('detalhes_pedido', pedido_id=pedido.pk)
    else:
        form = PedidoForm()
    return render(request, 'cadastrar_pedido.html', {'form': form})

def cadastrar_item_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'POST':
        form = ItemPedidoForm(request.POST)
        if form.is_valid():
            produto = form.cleaned_data['cod_prod']
            quantidade = form.cleaned_data['quantidade']
            preco = form.cleaned_data['preco']
            data_vencimento = form.cleaned_data['data_vencimento']

            # Verifica se já existe um item do mesmo produto no pedido
            item_existente = ItensPedido.objects.filter(cod_pedido=pedido, cod_prod=produto).first()

            if item_existente:
                # Atualiza a quantidade do item existente
                item_existente.quantidade += quantidade
                item_existente.save()
            else:
                # Cria um novo item
                item = ItensPedido(cod_pedido=pedido, cod_prod=produto, quantidade=quantidade, preco=preco,
                                   data_vencimento=data_vencimento)
                item.save()

            return redirect('detalhes_pedido', pedido_id=pedido.pk)
    else:
        print('nao entrou POST')

        form = ItemPedidoForm()
    print('chamando cadastrar html')

    return render(request, 'cadastrar_item_pedido.html', {'form': form, 'pedido': pedido})

def listar_itens_pedido(request):
    itens_pedido = ItensPedido.objects.all()
    return render(request, 'listar_itens_pedido.html', {'itens_pedido': itens_pedido})



def get_preco(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    return JsonResponse({'preco_custo': produto.preco_custo})




""" N U T R I   ***   N U T R I   ***   N U T R I   ***   N U T R I   ***   N U T R I   ***   """

def cadastrar_tabela_nutricional_produto(request):
    if request.method == 'POST':
        form = TabelaNutricionalProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tabelas_nutricionais_produtos')
    else:
        form = TabelaNutricionalProdutoForm()
    return render(request, 'cadastrar_tabela_nutricional_produto.html', {'form': form})

def listar_tabelas_nutricionais_produto(request):
    tabelas_nutricionais_produto = TabelaNutricionalProduto.objects.all()
    return render(request, 'listar_tabelas_nutricionais_produto.html', {'tabelas_nutricionais_produtos': tabelas_nutricionais_produto})


def cadastrar_ingrediente(request):
    if request.method == 'POST':
        form = ItemIngredienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ingredientes')  # Redirecionar para a lista de ingredientes após o cadastro
    else:
        form = ItemIngredienteForm()
    return render(request, 'cadastrar_ingrediente.html', {'form': form})

def listar_itens_nutricionais(request):
    itens_nutricionais = ItemTabelaNutricional.objects.all()
    return render(request, 'listar_itens_nutricionais.html', {'itens_nutricionais': itens_nutricionais})

def cadastrar_item_nutricional(request):
    if request.method == 'POST':
        form = ItemTabelaNutricionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_itens_nutricionais')
    else:
        form = ItemTabelaNutricionalForm()
    return render(request, 'cadastrar_item_nutricional.html', {'form': form})

def listar_tabelas_nutricionais(request):
    tabelas_nutricionais = TabelaNutricionalProduto.objects.all()
    return render(request, 'listar_tabelas_nutricionais.html', {'tabelas_nutricionais': tabelas_nutricionais})

def cadastrar_tabela_nutricional(request):
    if request.method == 'POST':
        form = TabelaNutricionalProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tabelas_nutricionais')
    else:
        form = TabelaNutricionalProdutoForm()
    return render(request, 'cadastrar_tabela_nutricional.html', {'form': form})

