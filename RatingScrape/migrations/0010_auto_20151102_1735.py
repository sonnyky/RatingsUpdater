# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0009_auto_20151102_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingstars',
            name='star_number',
            field=models.DecimalField(decimal_places=1, default=9.9, max_digits=2),
        ),
        migrations.AlterField(
            model_name='ratingstars',
            name='text',
            field=models.CharField(max_length=255, default='Default'),
        ),
        migrations.AlterField(
            model_name='ratingstars',
            name='title',
            field=models.CharField(max_length=255, default='Default'),
        ),
    ]
