# Generated by Django 4.2.3 on 2023-08-06 14:45

import GestaoOrcamento.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoOrcamento', '0002_orcamento_contrato'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='clausulas',
            field=models.TextField(default='CLAUSULA'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='inicio',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='servicos',
            field=models.TextField(default='SERVICO'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='termino',
            field=models.DateField(default=GestaoOrcamento.models.get_default_termino),
        ),
    ]
