# Generated by Django 3.1.3 on 2021-01-08 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0011_commission_dollar'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='ae_commission_rate',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7, verbose_name='Platform Komisyon Oranı'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commission',
            name='affiliate',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7, verbose_name='Affiliate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commission',
            name='coupon',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7, verbose_name='Kuponlar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commission',
            name='customs',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7, verbose_name='Gümrük Vergisi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commission',
            name='logistics',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7, verbose_name='Lojistik'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commission',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7, verbose_name='KDV'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commission',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Ağırlık'),
        ),
        migrations.AddField(
            model_name='commission',
            name='y_cargo',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7, verbose_name='Yurtiçi Kargo'),
            preserve_default=False,
        ),
    ]