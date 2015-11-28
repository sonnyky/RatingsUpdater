# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0002_reviewcomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewcomments',
            name='author',
            field=models.TextField(default='DEFAULT', max_length=255),
        ),
        migrations.AlterField(
            model_name='reviewcomments',
            name='comment',
            field=models.TextField(default='DEFAULT', max_length=255),
        ),
    ]
