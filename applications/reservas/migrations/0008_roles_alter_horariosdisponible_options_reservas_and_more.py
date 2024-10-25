# Generated by Django 5.0.2 on 2024-10-24 20:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0007_horariosdisponible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=120, verbose_name='Nombre')),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.AlterModelOptions(
            name='horariosdisponible',
            options={},
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=21, verbose_name='Estado')),
                ('comentarios', models.CharField(max_length=255, verbose_name='Comentarios')),
                ('id_espacio', models.ForeignKey(db_column='id_espacio', on_delete=django.db.models.deletion.CASCADE, to='reservas.espacios')),
            ],
            options={
                'db_table': 'reservas',
            },
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=21, verbose_name='Estado_pago')),
                ('id_metodo', models.ForeignKey(db_column='id_metodo_pago', on_delete=django.db.models.deletion.CASCADE, to='reservas.metodospago')),
                ('id_reserva', models.ForeignKey(db_column='id_reserva', on_delete=django.db.models.deletion.CASCADE, to='reservas.reservas')),
            ],
            options={
                'db_table': 'pagos',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=120, verbose_name='Nombre')),
                ('email', models.CharField(max_length=21, verbose_name='Email')),
                ('password', models.CharField(max_length=30, verbose_name='password')),
                ('direccion', models.CharField(max_length=51, verbose_name='Direccion')),
                ('id_rol', models.ForeignKey(db_column='id_rol', on_delete=django.db.models.deletion.CASCADE, to='reservas.roles')),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
        migrations.AddField(
            model_name='reservas',
            name='id_usuario',
            field=models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.CASCADE, to='reservas.usuarios'),
        ),
    ]