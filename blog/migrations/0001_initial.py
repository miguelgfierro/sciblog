# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=200, editable=False, blank=True)),
                ('abstract', models.TextField(blank=True)),
                ('pub_date', models.DateField(verbose_name=b'Date published')),
                ('keywords', models.CharField(max_length=100, blank=True)),
                ('author', models.CharField(max_length=100, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=blog.models.generate_filename, blank=True)),
                ('image_caption', models.CharField(max_length=200, blank=True)),
                ('body_page1_col1', models.TextField()),
                ('body_page1_col1_html', models.TextField(null=True, editable=False, blank=True)),
                ('body_page1_col2', models.TextField()),
                ('body_page1_col2_html', models.TextField(null=True, editable=False, blank=True)),
                ('body_page2_col1', models.TextField(blank=True)),
                ('body_page2_col1_html', models.TextField(null=True, editable=False, blank=True)),
                ('body_page2_col2', models.TextField(blank=True)),
                ('body_page2_col2_html', models.TextField(null=True, editable=False, blank=True)),
                ('site', models.ForeignKey(blank=True, to='sites.Site', null=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
            bases=(models.Model,),
        ),
    ]
