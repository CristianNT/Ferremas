# Generated by Django 5.0.6 on 2024-06-13 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=100, unique=True)),
                ('contrasenya', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('cliente', models.CharField(max_length=50)),
                ('empleado', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField()),
                ('total', models.PositiveIntegerField()),
                ('ubicacion', models.CharField(max_length=100)),
            ],
        ),
    ]
