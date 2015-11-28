# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewComments',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('author', models.TextField(max_length=255, default='DEFAULT_AUTHOR')),
                ('comment', models.TextField(max_length=255, default='DEFAULT_COMMENT')),
            ],
        ),
    ]
