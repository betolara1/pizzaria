# Generated by Django 4.2.7 on 2024-03-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_sobre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sobre',
            name='descricao',
            field=models.TextField(),
        ),
    ]
