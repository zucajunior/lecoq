# Generated by Django 4.1 on 2023-08-11 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lecoq2", "0007_itenspedido_preco_pedido_valor"),
    ]

    operations = [
        migrations.AddField(
            model_name="itenspedido",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
