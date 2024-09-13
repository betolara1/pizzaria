# Generated by Django 4.2.7 on 2024-04-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_pedidos_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='status',
            field=models.CharField(choices=[('1', 'Pendente'), ('2', 'Em Preparo'), ('3', 'Pronto'), ('4', 'Cancelado')], max_length=1, null=True),
        ),
    ]
