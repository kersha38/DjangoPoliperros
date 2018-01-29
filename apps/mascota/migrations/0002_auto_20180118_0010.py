# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-01-18 05:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0001_initial'),
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicina', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Visita_Medica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('diagnostico', models.TextField()),
                ('peso', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='mascota',
            old_name='fecha_rescate',
            new_name='fecha_ingreso',
        ),
        migrations.AddField(
            model_name='mascota',
            name='color',
            field=models.CharField(default=2016, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mascota',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adopcion.Persona'),
        ),
        migrations.AddField(
            model_name='visita_medica',
            name='mascota',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascota.Mascota'),
        ),
        migrations.AddField(
            model_name='visita_medica',
            name='medicina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascota.Medicina'),
        ),
    ]