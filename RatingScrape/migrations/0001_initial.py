# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStars',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('star_number', models.IntegerField(max_length=20)),
                ('pub_date', models.DateTimeField(verbose_name='date this is published')),
            ],
        ),
    ]
