# Generated by Django 3.1.3 on 2020-12-29 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20201230_0137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipping',
            old_name='trancking_number',
            new_name='tracking_number',
        ),
    ]