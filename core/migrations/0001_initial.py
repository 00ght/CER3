# Generated by Django 4.2.5 on 2023-11-25 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('C_USM', 'Comunidad_USM'), ('E', 'Estudiante'), ('P', 'Profesor'), ('J', 'Jefe_de_Carrera')], max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('fecha_termino', models.DateTimeField(auto_now_add=True)),
                ('Titulo', models.CharField(max_length=55)),
                ('Descripcion', models.CharField(max_length=105)),
                ('Tipo', models.CharField(choices=[('V', 'Vacaciones'), ('F', 'Feriado'), ('S_A', 'Suspension_de_actividades'), ('S_A_PM', 'Suspension_de_actividades_PM'), ('P', 'Periodo_Lectivo'), ('S_E', 'Suspension_de_evaluaciones'), ('C', 'Ceremonia'), ('E', 'EDDA'), ('A', 'Ayudantias'), ('H', 'Hito_Academico'), ('S', 'Secretaria_Academica'), ('Q', 'QAI')], max_length=30)),
                ('Segmento', models.ManyToManyField(related_name='Segmentos_evento', to='core.segmento')),
            ],
        ),
    ]
