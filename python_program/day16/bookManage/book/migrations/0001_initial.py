# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('price', models.IntegerField()),
                ('author', models.CharField(max_length=32)),
                ('publiosh', models.CharField(max_length=32)),
                ('info', models.CharField(max_length=1024)),
            ],
        ),
    ]
