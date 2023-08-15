# Generated by Django 4.1 on 2023-08-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lecoq2", "0003_rename_peso_tabelanutricionalproduto_valor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="cnpj",
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="ddd",
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="endereco",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="hora_abertura",
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="hora_fechamento",
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="responsavel",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="whats",
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
