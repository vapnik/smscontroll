# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0005_onesms_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='average_time',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='cost',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='last_time',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='optimal_rules',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
