# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Componentes',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('instrumento', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Concierto',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('lugar', models.CharField(max_length=32)),
                ('precio', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('constitucion', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='concierto',
            name='grupo',
            field=models.ForeignKey(to='conciertos.Grupo'),
        ),
        migrations.AddField(
            model_name='componentes',
            name='grupo',
            field=models.ForeignKey(to='conciertos.Grupo'),
        ),
    ]
