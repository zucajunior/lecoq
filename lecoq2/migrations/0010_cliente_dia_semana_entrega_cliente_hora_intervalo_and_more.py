# Generated by Django 4.1 on 2023-08-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lecoq2", "0009_remove_itenspedido_total"),
    ]

    operations = [
        migrations.AddField(
            model_name="cliente",
            name="dia_semana_entrega",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="cliente",
            name="hora_intervalo",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="cliente",
            name="hora_intervalo2",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="cliente",
            name="nome_funcionaria_responsavel",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="cliente",
            name="whats_cantina",
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
