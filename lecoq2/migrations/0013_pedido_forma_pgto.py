# Generated by Django 4.1 on 2023-09-12 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lecoq2", "0012_itenspedido_quantidade_dev"),
    ]

    operations = [
        migrations.AddField(
            model_name="pedido",
            name="forma_pgto",
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]