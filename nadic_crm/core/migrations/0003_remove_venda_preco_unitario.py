# Generated by Django 5.0.2 on 2024-03-05 13:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_venda_preco_unitario"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="venda",
            name="preco_unitario",
        ),
    ]