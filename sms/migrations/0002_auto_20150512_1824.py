# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onesms',
            name='receive_time',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
    ]
