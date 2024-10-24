# Generated by Django 5.0.2 on 2024-10-24 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0005_alter_espacios_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetodosPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_metodo', models.CharField(max_length=50, verbose_name='Nombre del metodo')),
            ],
            options={
                'db_table': 'metodos_pago',
                'managed': False,
            },
        ),
    ]
