# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-17 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Question')),
                ('answer', models.CharField(max_length=255, verbose_name='Answer')),
                ('verify', models.BooleanField(default=False, verbose_name='Verify')),
            ],
            options={
                'verbose_name_plural': 'IA',
            },
        ),
    ]