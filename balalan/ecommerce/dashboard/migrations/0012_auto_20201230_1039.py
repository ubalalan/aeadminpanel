# Generated by Django 3.1.3 on 2020-12-30 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_track_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Oluşturulma Tarihi'),
        ),
    ]
