# Generated by Django 4.1 on 2023-08-05 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                ("codigo", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=100)),
                ("endereco", models.CharField(max_length=200)),
                ("responsavel", models.CharField(max_length=100)),
                ("cnpj", models.CharField(max_length=14)),
                ("whats", models.CharField(max_length=11)),
                ("ddd", models.CharField(max_length=2)),
                ("hora_abertura", models.TimeField()),
                ("hora_fechamento", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Ingredientes",
            fields=[
                ("codigo", models.AutoField(primary_key=True, serialize=False)),
                ("ordem", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="TabelaNutricional",
            fields=[
                ("cod", models.AutoField(primary_key=True, serialize=False)),
                ("descricao", models.CharField(max_length=100)),
                ("peso", models.DecimalField(decimal_places=2, max_digits=6)),
                ("porcentagem", models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name="Produto",
            fields=[
                ("codigo", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=100)),
                ("preco1", models.DecimalField(decimal_places=2, max_digits=10)),
                ("preco2", models.DecimalField(decimal_places=2, max_digits=10)),
                ("preco3", models.DecimalField(decimal_places=2, max_digits=10)),
                ("preco_custo", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "valor_energetico",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
                ("porcao", models.PositiveIntegerField()),
                ("peso", models.DecimalField(decimal_places=2, max_digits=6)),
                ("dias_validade", models.PositiveIntegerField()),
                (
                    "codigo_tabela_ingredientes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lecoq2.ingredientes",
                    ),
                ),
                (
                    "codigo_tabela_nutricional",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lecoq2.tabelanutricional",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pedido",
            fields=[
                ("codigo", models.AutoField(primary_key=True, serialize=False)),
                ("data_entrega", models.DateField()),
                ("observacao", models.TextField(max_length=300)),
                ("faturado", models.BooleanField(default=False)),
                (
                    "cod_cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="lecoq2.cliente"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItensPedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantidade", models.PositiveIntegerField()),
                ("data_vencimento", models.DateField()),
                (
                    "cod_pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="lecoq2.pedido"
                    ),
                ),
                (
                    "cod_prod",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="lecoq2.produto"
                    ),
                ),
            ],
        ),
    ]
