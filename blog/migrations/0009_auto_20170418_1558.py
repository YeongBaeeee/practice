# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 06:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170417_0309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='massage',
            new_name='message',
        ),
    ]