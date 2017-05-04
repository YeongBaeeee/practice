# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0010_auto_20170503_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameuser',
            name='server_name',
            field=models.CharField(choices=[('A', 'A서버'), ('B', 'B서버'), ('C', 'C서버')], max_length=10),
        ),
        migrations.AlterField(
            model_name='gameuser',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
