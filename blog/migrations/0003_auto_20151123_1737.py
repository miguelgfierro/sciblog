# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151123_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='section',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
