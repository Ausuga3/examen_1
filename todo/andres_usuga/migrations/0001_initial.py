# Generated by Django 5.1.1 on 2024-11-20 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254, verbose_name='Nombre de la tarea')),
                ('estado', models.IntegerField(blank=True, choices=[(0, 'Nuevas'), (1, 'Terminadas'), (2, 'Eliminadas')], default=0)),
            ],
        ),
    ]
