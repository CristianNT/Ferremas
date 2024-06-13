# Generated by Django 5.0.6 on 2024-06-13 03:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('empleado', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('fecha_prep', models.DateTimeField(null=True)),
                ('fecha_extr', models.DateTimeField(null=True)),
                ('fecha_desp', models.DateTimeField(null=True)),
                ('fecha_entr', models.DateTimeField(null=True)),
                ('estado', models.CharField(max_length=30)),
                ('compra', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=50)),
                ('stock', models.PositiveIntegerField()),
                ('precio', models.PositiveIntegerField()),
                ('descuento', models.PositiveSmallIntegerField(null=True)),
                ('descripcion', models.TextField()),
                ('imagen', models.CharField(max_length=500)),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.sede')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('run', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=100, unique=True)),
                ('tipo', models.CharField(max_length=50)),
                ('contrasenya', models.CharField(max_length=20)),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.sede')),
            ],
        ),
    ]