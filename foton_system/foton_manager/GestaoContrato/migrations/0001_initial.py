# Generated by Django 4.2.3 on 2023-07-19 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('GestaoCliente', '0001_initial'),
        ('GestaoOrcamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('numero', models.CharField(default=0, max_length=100)),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contratoCliente', to='GestaoCliente.cliente')),
                ('orcamento', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orcamentoCliente', to='GestaoOrcamento.orcamento')),
            ],
        ),
    ]