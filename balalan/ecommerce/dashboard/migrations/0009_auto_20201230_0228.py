# Generated by Django 3.1.3 on 2020-12-29 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20201230_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='coupon',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Kuponlar'),
        ),
    ]