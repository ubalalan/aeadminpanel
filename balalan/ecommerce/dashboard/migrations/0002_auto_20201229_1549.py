# Generated by Django 3.1.3 on 2020-12-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='İndirim Fiyatı'),
        ),
        migrations.AlterField(
            model_name='track',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Fiyat'),
        ),
    ]
