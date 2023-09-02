# Generated by Django 4.2.3 on 2023-08-07 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoOrcamento', '0003_orcamento_clausulas_orcamento_inicio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComposicaoCusto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('descricao', models.TextField()),
                ('custo', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='orcamento',
            name='base_dados',
            field=models.CharField(choices=[('SINAPI', 'SINAPI'), ('TCPO', 'TCPO'), ('GOINFRA', 'GOINFRA'), ('DNIT', 'DNIT'), ('FOTON', 'FOTON')], default='BASE', max_length=50),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='codigo_bim',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='eficiencia',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='nome',
            field=models.CharField(default='NOME', max_length=255),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='unidade_de_medida',
            field=models.CharField(default='UN', max_length=50),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='descricao',
            field=models.TextField(default='DESCRICAO'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='composicoes_custo',
            field=models.ManyToManyField(to='GestaoOrcamento.composicaocusto'),
        ),
    ]