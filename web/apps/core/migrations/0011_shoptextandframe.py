# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-06-12 18:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('core', '0010_auto_20190611_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopTextAndFrame',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='core_shoptextandframe', serialize=False, to='cms.CMSPlugin')),
                ('text', djangocms_text_ckeditor.fields.HTMLField()),
                ('frame_text', models.TextField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
