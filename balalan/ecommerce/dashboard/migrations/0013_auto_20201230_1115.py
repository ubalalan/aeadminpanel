# Generated by Django 3.1.3 on 2020-12-30 08:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20201230_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Oluşturulma Tarihi'),
        ),
    ]
