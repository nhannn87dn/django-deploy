# Generated by Django 5.0.1 on 2024-02-27 03:49

import product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_thumbnail_alter_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default=None, null=True, upload_to=product.models.get_upload_to),
        ),
    ]
