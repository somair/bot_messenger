# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-17 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name App')),
                ('token', models.CharField(max_length=255, verbose_name='Token Page')),
                ('verify_token', models.CharField(max_length=255, verbose_name='Verify Token')),
            ],
            options={
                'verbose_name_plural': 'Facebook',
            },
        ),
    ]