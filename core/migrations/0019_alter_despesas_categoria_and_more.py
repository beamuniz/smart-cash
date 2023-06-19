# Generated by Django 4.2.2 on 2023-06-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_despesas_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesas',
            name='categoria',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='despesas',
            name='dataPagamento',
            field=models.DateField(blank=True, null=True, verbose_name='DataPagamento'),
        ),
        migrations.AlterField(
            model_name='despesas',
            name='dataVencimento',
            field=models.DateField(blank=True, null=True, verbose_name='DataVencimento'),
        ),
    ]
