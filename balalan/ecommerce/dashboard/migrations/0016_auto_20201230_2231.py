# Generated by Django 3.1.3 on 2020-12-30 19:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='decription',
            field=models.CharField(max_length=5000, null=True, verbose_name='Ürün Açıklaması'),
        ),
        migrations.AlterField(
            model_name='track',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Oluşturulma Tarihi'),
        ),
    ]
