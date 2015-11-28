# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0003_auto_20151129_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReviewComments',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('author', models.TextField(max_length=255, default='DEFAULT')),
                ('comment', models.TextField(max_length=255, default='DEFAULT')),
            ],
        ),
        migrations.DeleteModel(
            name='ReviewComments',
        ),
    ]
