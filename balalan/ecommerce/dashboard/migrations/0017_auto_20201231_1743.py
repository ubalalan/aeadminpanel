# Generated by Django 3.1.3 on 2020-12-31 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20201230_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commission',
            name='product',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
        migrations.DeleteModel(
            name='Commission',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Shipping',
        ),
    ]
