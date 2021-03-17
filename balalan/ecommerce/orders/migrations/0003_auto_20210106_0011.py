# Generated by Django 3.1.3 on 2021-01-05 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(choices=[('Gümrük İşlemleri', 'Gümrük İşlemleri'), ('Yolda', 'Yolda'), ('Teslim Edildi', 'Teslim Edildi')], default=False, verbose_name='Sipariş Durumu'),
        ),
    ]
