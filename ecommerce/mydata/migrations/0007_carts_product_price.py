# Generated by Django 4.2.2 on 2023-07-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0006_carts_product_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='product_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
