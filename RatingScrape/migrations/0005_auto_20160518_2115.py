# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0004_auto_20151129_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreviewcomments',
            name='rating_given_by_user',
            field=models.TextField(max_length=255, default='DEFAULT'),
        ),
        migrations.AddField(
            model_name='userreviewcomments',
            name='review_id',
            field=models.TextField(max_length=255, default='DEFAULT'),
        ),
        migrations.AddField(
            model_name='userreviewcomments',
            name='version_rated',
            field=models.TextField(max_length=255, default='DEFAULT'),
        ),
    ]
