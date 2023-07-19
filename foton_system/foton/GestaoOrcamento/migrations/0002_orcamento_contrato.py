# Generated by Django 4.2.3 on 2023-07-19 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoContrato', '0001_initial'),
        ('GestaoOrcamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='contrato',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orcamentoContrato', to='GestaoContrato.contrato'),
        ),
    ]