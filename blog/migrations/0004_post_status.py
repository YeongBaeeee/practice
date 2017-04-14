# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170414_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='d', max_length=1),
            preserve_default=False,
        ),
    ]