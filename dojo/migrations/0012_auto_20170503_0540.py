# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0011_auto_20170503_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameuser',
            name='server_name',
            field=models.CharField(max_length=5),
        ),
    ]
