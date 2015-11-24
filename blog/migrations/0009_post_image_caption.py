# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20151124_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_caption',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
