# Generated by Django 3.1.3 on 2021-01-10 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0014_auto_20210111_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='dollar',
            field=models.FloatField(verbose_name='Kur Fiyatı'),
        ),
    ]
