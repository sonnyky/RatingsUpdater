# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingstars',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='ratingstars',
            name='star_number',
        ),
    ]
