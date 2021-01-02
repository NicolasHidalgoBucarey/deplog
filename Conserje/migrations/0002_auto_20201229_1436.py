# Generated by Django 3.1.2 on 2020-12-29 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Conserje', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numero', models.IntegerField()),
                ('Propietario', models.CharField(max_length=100)),
                ('Residente', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='Fecha',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='Hora',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='encomienda',
            name='Fecha',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='encomienda',
            name='Hora',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='Departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Conserje.departamento'),
        ),
    ]