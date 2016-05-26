# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0005_auto_20160518_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='AndroidRatingStars',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('star_number', models.TextField(default='Default', max_length=255)),
                ('time_stamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
