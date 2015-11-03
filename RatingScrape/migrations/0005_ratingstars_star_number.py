# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0004_ratingstars_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingstars',
            name='star_number',
            field=models.IntegerField(default=1.5),
        ),
    ]
