# Generated by Django 4.2.2 on 2023-06-19 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_contabancaria_id_contabancaria'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesas',
            name='id_despesa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.contabancaria', verbose_name='id despesa'),
        ),
    ]
