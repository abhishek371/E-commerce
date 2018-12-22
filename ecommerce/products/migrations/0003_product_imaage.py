# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-22 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imaage',
            field=models.FileField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
    ]