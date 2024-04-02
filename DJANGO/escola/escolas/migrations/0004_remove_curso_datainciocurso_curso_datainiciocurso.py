# Generated by Django 5.0.2 on 2024-03-04 20:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0003_alter_aluno_cpf_alter_aluno_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='dataIncioCurso',
        ),
        migrations.AddField(
            model_name='curso',
            name='dataInicioCurso',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
