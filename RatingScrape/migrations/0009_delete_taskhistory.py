# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0008_taskhistory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TaskHistory',
        ),
    ]
