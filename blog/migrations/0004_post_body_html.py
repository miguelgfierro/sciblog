# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151123_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_html',
            field=models.TextField(null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
