# Generated by Django 5.0.2 on 2024-03-04 20:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0004_remove_curso_datainciocurso_curso_datainiciocurso'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='dataFimCurso',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
