# Generated by Django 3.1.3 on 2021-01-04 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0002_auto_20210105_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commission',
            name='ae_remaining',
        ),
        migrations.RemoveField(
            model_name='commission',
            name='net_profit',
        ),
        migrations.RemoveField(
            model_name='commission',
            name='net_profit_tl',
        ),
        migrations.RemoveField(
            model_name='commission',
            name='profit_margin',
        ),
    ]