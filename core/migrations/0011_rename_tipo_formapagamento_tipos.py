# Generated by Django 4.2.2 on 2023-06-18 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_despesas_nome_alter_formapagamento_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formapagamento',
            old_name='tipo',
            new_name='tipos',
        ),
    ]