# Generated by Django 3.1.3 on 2021-01-15 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0016_auto_20210111_0116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commission',
            old_name='affiliate',
            new_name='affiliate_rate',
        ),
    ]