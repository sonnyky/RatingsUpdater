# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0006_androidratingstars'),
    ]

    operations = [
        migrations.CreateModel(
            name='AndroidUserReviewComments',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('author', models.TextField(max_length=255, default='DEFAULT')),
                ('comment', models.TextField(max_length=255, default='DEFAULT')),
                ('rating_given_by_user', models.TextField(max_length=255, default='DEFAULT')),
            ],
        ),
    ]
