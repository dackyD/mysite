# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-21 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_Specials',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='sampleplugin_daily_specials', serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='daily_specials')),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Daily Special',
                'verbose_name_plural': 'Daily Specials',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Menu_Item',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='sampleplugin_menu_item', serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='menu_items')),
                ('price', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
