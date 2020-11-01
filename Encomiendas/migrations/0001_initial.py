# Generated by Django 3.1.2 on 2020-11-01 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='encomienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=120)),
                ('Fecha', models.DateField()),
                ('Hora', models.TimeField()),
                ('Información', models.TextField()),
                ('Recibido', models.BooleanField(default=False)),
            ],
        ),
    ]