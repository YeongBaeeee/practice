# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0005_auto_20170503_0118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gameuser',
            old_name='servername',
            new_name='server_name',
        ),
        migrations.AlterUniqueTogether(
            name='gameuser',
            unique_together=set([('server_name', 'username')]),
        ),
    ]
