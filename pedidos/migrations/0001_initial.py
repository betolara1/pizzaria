# Generated by Django 4.2.7 on 2024-04-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cardapio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='imagens_pizzas/')),
            ],
        ),
        migrations.CreateModel(
            name='Sabores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tamanho', models.CharField(choices=[('B', 'Broto'), ('P', 'Pequena'), ('M', 'Média'), ('G', 'Grande'), ('F', 'Família')], max_length=1)),
                ('observacao', models.CharField(max_length=100, null=True)),
                ('sabores', models.ManyToManyField(to='pedidos.sabores')),
            ],
        ),
    ]
