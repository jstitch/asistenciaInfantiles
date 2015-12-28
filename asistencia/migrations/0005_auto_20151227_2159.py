# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 03:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0004_auto_20151227_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10, unique=True)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='encuentro',
            name='ciclo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asistencia.Ciclo'),
        ),
    ]
