# Generated by Django 5.1.5 on 2025-02-14 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos_almacen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='material',
            field=models.JSONField(default=list),
        ),
    ]
