# Generated by Django 4.0.6 on 2022-09-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('obras', models.CharField(max_length=120)),
                ('Estilo', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='ObraDeArte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('anio', models.IntegerField(max_length=60)),
                ('Estilo', models.CharField(max_length=80)),
            ],
        ),
    ]
