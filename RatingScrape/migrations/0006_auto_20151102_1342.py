# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0005_ratingstars_star_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingstars',
            name='star_number',
            field=models.DecimalField(default=2.5, decimal_places=1, max_digits=2),
        ),
    ]
