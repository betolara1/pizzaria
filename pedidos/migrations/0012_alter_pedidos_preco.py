# Generated by Django 5.0.7 on 2024-08-10 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0011_remove_pedidos_preco_alter_pedidos_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='preco',
            field=models.FloatField(),
        ),
    ]
