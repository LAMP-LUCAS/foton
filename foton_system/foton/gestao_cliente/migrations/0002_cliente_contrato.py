# Generated by Django 4.2.3 on 2023-07-18 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_contrato', '0001_initial'),
        ('gestao_cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='contrato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contratos', to='gestao_contrato.contrato'),
        ),
    ]