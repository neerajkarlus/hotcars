# Generated by Django 4.1.4 on 2023-02-08 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0028_order_balance_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='accssamt',
            field=models.FloatField(default=None, null=True, verbose_name='Sum Total Of Car'),
        ),
        migrations.AddField(
            model_name='order',
            name='insuramt',
            field=models.FloatField(default=None, null=True, verbose_name='Sum Total Of Car'),
        ),
        migrations.AddField(
            model_name='order',
            name='regst_amt',
            field=models.FloatField(default=None, null=True, verbose_name='Sum Total Of Car'),
        ),
        migrations.AddField(
            model_name='order',
            name='road_tax',
            field=models.FloatField(default=None, null=True, verbose_name='Sum Total Of Car'),
        ),
    ]