# Generated by Django 3.1.2 on 2020-11-01 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bitacoras', '0002_bitacora_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitacora',
            name='Departamento',
            field=models.IntegerField(),
        ),
    ]