# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-22 21:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_imaage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imaage',
            new_name='image',
        ),
    ]
