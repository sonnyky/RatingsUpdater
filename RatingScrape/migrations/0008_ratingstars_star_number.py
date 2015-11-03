# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0007_remove_ratingstars_star_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingstars',
            name='star_number',
            field=models.DecimalField(max_digits=2, default=3.7, decimal_places=1),
        ),
    ]
