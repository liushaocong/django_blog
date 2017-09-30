# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('create_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='biji',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('href', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='jsbooks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=64)),
                ('body', models.TextField()),
            ],
        ),
    ]
