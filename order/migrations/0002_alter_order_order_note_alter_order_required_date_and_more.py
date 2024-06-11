# Generated by Django 4.2.13 on 2024-06-07 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_note',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='required_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipped_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='staff',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
