# Generated by Django 3.1.3 on 2020-12-29 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20201229_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='decription',
        ),
        migrations.RemoveField(
            model_name='track',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='track',
            name='images',
        ),
        migrations.RemoveField(
            model_name='track',
            name='link',
        ),
        migrations.AlterField(
            model_name='track',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Fiyat'),
        ),
    ]