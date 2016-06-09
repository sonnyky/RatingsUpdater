# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('RatingScrape', '0007_androiduserreviewcomments'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Task name', max_length=100, help_text='Select a task to record')),
                ('history', jsonfield.fields.JSONField(verbose_name='history', default={}, help_text='JSON containing the tasks history')),
            ],
            options={
                'verbose_name': 'Task History',
                'verbose_name_plural': 'Task Histories',
            },
        ),
    ]
