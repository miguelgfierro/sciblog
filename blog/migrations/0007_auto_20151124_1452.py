# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='body_page1_col1',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='body_html',
            new_name='body_page1_col1_html',
        ),
        migrations.AddField(
            model_name='post',
            name='body_page1_col2',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='body_page1_col2_html',
            field=models.TextField(null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='body_page2_col1',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='body_page2_col1_html',
            field=models.TextField(null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='body_page2_col2',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='body_page2_col2_html',
            field=models.TextField(null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
