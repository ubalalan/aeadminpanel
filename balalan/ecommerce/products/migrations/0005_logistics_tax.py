# Generated by Django 3.1.3 on 2021-01-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_delete_suply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domestic_shipping_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='PTS Teslim Fiyatı')),
                ('logistic_shipping_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Lojistik Fiyatı')),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customs_tax', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Gümrük Ücreti')),
                ('kdv', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='KDV')),
            ],
        ),
    ]
