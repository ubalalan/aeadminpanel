# Generated by Django 3.1.3 on 2020-12-30 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_remove_commission_sale_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Oluşturulma Tarihi'),
        ),
    ]