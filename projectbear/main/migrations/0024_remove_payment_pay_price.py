# Generated by Django 3.0.5 on 2020-04-24 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_payment_pay_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='pay_price',
        ),
    ]
