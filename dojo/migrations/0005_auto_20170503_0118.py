# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0004_auto_20170503_0105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gameuser',
            old_name='server_name',
            new_name='servername',
        ),
        migrations.AlterUniqueTogether(
            name='gameuser',
            unique_together=set([]),
        ),
    ]
