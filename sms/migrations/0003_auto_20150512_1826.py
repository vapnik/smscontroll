# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20150512_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onesms',
            name='receive_time',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
