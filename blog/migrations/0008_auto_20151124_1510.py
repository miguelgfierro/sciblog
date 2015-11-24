# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20151124_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body_page1_col2',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
