# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_auto_20150512_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='apiKey',
            field=models.CharField(null=True, max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='login',
            field=models.CharField(null=True, max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='password',
            field=models.CharField(null=True, max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='link',
            field=models.CharField(null=True, max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
