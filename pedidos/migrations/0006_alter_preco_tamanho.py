# Generated by Django 4.2.7 on 2024-04-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preco',
            name='tamanho',
            field=models.CharField(choices=[('B', 'Broto'), ('P', 'Pequena'), ('M', 'Média'), ('G', 'Grande'), ('F', 'Família')], max_length=1),
        ),
    ]
