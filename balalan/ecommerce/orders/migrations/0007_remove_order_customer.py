# Generated by Django 3.1.7 on 2021-03-18 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]