# Generated by Django 4.1 on 2022-09-14 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetointegrador', '0002_remove_curriculo_escolaridade_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='categoria',
            new_name='vagas',
        ),
    ]
