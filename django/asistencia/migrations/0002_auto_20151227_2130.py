# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Encuentro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('participantes', models.ManyToManyField(through='asistencia.Asistencia', to='asistencia.Participante')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='asistencia',
            name='encuentro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.Encuentro'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.Equipo'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='participante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.Participante'),
        ),
    ]
