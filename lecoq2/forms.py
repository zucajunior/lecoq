from django import forms
from .models import Cliente, Produto,  ItemIngrediente, ItemTabelaNutricional, Pedido, ItensPedido, Ingrediente,\
    TabelaNutricionalProduto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'  # Incluir todos os campos do modelo Produto

class ItemIngredienteForm(forms.ModelForm):
    class Meta:
        model = ItemIngrediente
        fields = '__all__'

class ItemTabelaNutricionalForm(forms.ModelForm):
    class Meta:
        model = ItemTabelaNutricional
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class TabelaNutricionalProdutoForm(forms.ModelForm):
    class Meta:
        model = TabelaNutricionalProduto
        fields = '__all__'

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItensPedido
        fields = '__all__'
