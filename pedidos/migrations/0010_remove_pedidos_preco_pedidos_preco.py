# Generated by Django 5.0.7 on 2024-08-10 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0009_pedidos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidos',
            name='preco',
        ),
        migrations.AddField(
            model_name='pedidos',
            name='preco',
            field=models.ManyToManyField(to='pedidos.preco'),
        ),
    ]
