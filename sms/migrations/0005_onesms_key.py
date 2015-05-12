# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0004_auto_20150512_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='onesms',
            name='key',
            field=models.CharField(max_length=12, default='null'),
            preserve_default=False,
        ),
    ]
