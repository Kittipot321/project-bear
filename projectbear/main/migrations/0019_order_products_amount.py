# Generated by Django 3.0.2 on 2020-04-19 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200418_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_products',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]