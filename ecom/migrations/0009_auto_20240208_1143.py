# Generated by Django 3.0.5 on 2024-02-08 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_auto_20240202_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='razorpay_signature',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]