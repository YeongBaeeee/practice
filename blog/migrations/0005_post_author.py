# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='관리자', max_length=50, verbose_name='작성자'),
            preserve_default=False,
        ),
    ]
