# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0002_auto_20151028_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingstars',
            name='title',
            field=models.CharField(default='楽天市場', max_length=255),
        ),
    ]
