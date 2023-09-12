from django.utils import timezone

from django.db import models
from django.db.models import F, Sum, DecimalField

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from decimal import Decimal



class ItemIngrediente(models.Model):
    codigo     = models.AutoField(primary_key=True)
    descricao  = models.CharField(max_length=100)

    def __str__(self):
        return str(self.descricao)


class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    preco1 = models.DecimalField(max_digits=10, decimal_places=2)
    preco2 = models.DecimalField(max_digits=10, decimal_places=2)
    preco3 = models.DecimalField(max_digits=10, decimal_places=2)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    valor_energetico = models.DecimalField(max_digits=6, decimal_places=2)
    porcao = models.PositiveIntegerField()
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    dias_validade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Ingrediente(models.Model):
    codigo_ingrediente = models.ForeignKey(ItemIngrediente, on_delete=models.CASCADE)
    codigo_prod = models.ForeignKey(Produto, on_delete=models.CASCADE)
    ordem  = models.PositiveIntegerField()

    def __str__(self):
        return f"ordem: {self.ordem} - Ingrediente: {self.codigo_ingrediente.descricao} - Produto {self.codigo_prod.nome}"


class ItemTabelaNutricional(models.Model):
    cod = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class TabelaNutricionalProduto(models.Model):
    codigo_nutri  = models.ForeignKey(ItemTabelaNutricional, on_delete=models.CASCADE)
    codigo_prod   = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor         = models.DecimalField(max_digits=6, decimal_places=2)
    porcentagemVD = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"item Nutricinal: {self.codigo_nutri.descricao} - Produto: {self.codigo_prod.nome}"


class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200, null=True,blank=True)
    responsavel = models.CharField(max_length=100, null=True,blank=True)
    cnpj = models.CharField(max_length=14,null=True, blank=True)
    whats = models.CharField(max_length=11, null=True,blank=True)
    ddd = models.CharField(max_length=2,null=True, blank=True)
    hora_abertura = models.TimeField(null=True, blank=True)
    hora_fechamento = models.TimeField(null=True,blank=True)
    hora_intervalo = models.TimeField(null=True, blank=True)
    hora_intervalo2 = models.TimeField(null=True, blank=True)
    dia_semana_entrega = models.CharField(max_length=30, null=True, blank=True)
    whats_cantina = models.CharField(max_length=11, null=True, blank=True)
    nome_funcionaria_responsavel = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    codigo         = models.AutoField(primary_key=True)
    cod_cliente    = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_entrega   = models.DateField()
    observacao     = models.TextField(max_length=300, null=True, blank=True)
    faturado       = models.BooleanField(default=False)
    valor          = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null= False)
    data_criacao   = models.DateTimeField(default=timezone.now)
    data_alteracao = models.DateTimeField(auto_now=True)
    forma_pgto     = models.TextField(max_length=50, null= True, blank= True)
    def __str__(self):
        return f"Pedido {self.codigo} - Cliente: {self.cod_cliente.nome} - Valor: {self.valor} - Produto {self.data_entrega} - Faturado: {self.faturado}"



class ItensPedido(models.Model):
    cod_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cod_prod = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    quantidade_dev  = models.PositiveIntegerField(default=0)
    data_vencimento = models.DateField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Pedido {self.cod_pedido.codigo} - Produto {self.cod_prod.nome}"

    def quantidade_cobrado(self):
        return self.quantidade - self.quantidade_dev

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Calculate and update the Pedido's valor field with the sum of all ItensPedido values
        total_value = ItensPedido.objects.filter(cod_pedido=self.cod_pedido).aggregate(
            total=Sum(F('quantidade') * F('preco') - F('quantidade_dev') * F('preco'), output_field=DecimalField()))[
            'total']

        Pedido.objects.filter(codigo=self.cod_pedido.codigo).update(valor=total_value or Decimal('0.00'))

    def calcular_valor_total(self):
        return (self.quantidade - self.quantidade_dev) * self.preco


@receiver([post_save, post_delete], sender=ItensPedido)
def update_pedido_alteracao(sender, instance, **kwargs):
    pedido = instance.cod_pedido
    pedido.data_alteracao = timezone.now()
    pedido.save()
