# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-06-10 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutHeadline',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='core_aboutheadline', serialize=False, to='cms.CMSPlugin')),
                ('title', models.TextField(max_length=1000)),
                ('subtitle', models.TextField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
