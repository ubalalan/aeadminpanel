# Generated by Django 3.1.3 on 2021-01-07 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_logistics_tax'),
        ('commissions', '0009_auto_20210107_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='ae_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product', verbose_name='Ürün Bilgisi'),
        ),
    ]