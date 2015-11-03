# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0010_auto_20151102_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingstars',
            name='time_stamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
