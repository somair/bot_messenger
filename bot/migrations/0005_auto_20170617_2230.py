# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-17 22:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_userfacebook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfacebook',
            old_name='recipient_id',
            new_name='sender_id',
        ),
    ]
