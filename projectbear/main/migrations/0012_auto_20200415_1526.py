# Generated by Django 3.0.2 on 2020-04-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200411_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='pay_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, default='product_pic/default.png', null=True, upload_to='product_pic'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='user/default_pic.png', null=True, upload_to='user'),
        ),
    ]