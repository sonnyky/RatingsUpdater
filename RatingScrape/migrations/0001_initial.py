# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStars',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=255, default='Default')),
                ('text', models.TextField(max_length=255, default='Default')),
                ('star_number', models.DecimalField(default=9.9, max_digits=2, decimal_places=1)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
        ),
    ]
