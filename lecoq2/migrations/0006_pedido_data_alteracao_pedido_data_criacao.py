# Generated by Django 4.1 on 2023-08-10 08:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("lecoq2", "0005_alter_cliente_cnpj_alter_cliente_ddd_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pedido",
            name="data_alteracao",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="pedido",
            name="data_criacao",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
