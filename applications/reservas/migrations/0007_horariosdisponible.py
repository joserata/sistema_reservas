# Generated by Django 5.0.2 on 2024-10-24 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0006_metodospago'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorariosDisponible',
            fields=[
                ('id_horario', models.IntegerField(primary_key=True, serialize=False)),
                ('dia_semana', models.CharField(max_length=20, verbose_name='Día de la semana')),
                ('hora_apertura', models.TimeField(verbose_name='Hora de apertura')),
                ('hora_cierre', models.TimeField(verbose_name='Hora de cierre')),
            ],
            options={
                'db_table': 'horarios_disponible',
                'managed': False,
            },
        ),
    ]