# Generated by Django 3.0.2 on 2020-04-03 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200403_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='product_pic'),
        ),
    ]
