# Generated by Django 4.2.2 on 2023-07-09 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0002_category_alter_products_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cart',
            new_name='Carts',
        ),
        migrations.RenameModel(
            old_name='category',
            new_name='Categorys',
        ),
        migrations.AlterModelOptions(
            name='carts',
            options={'verbose_name_plural': 'Carts'},
        ),
        migrations.AlterModelOptions(
            name='categorys',
            options={'verbose_name_plural': 'Categorys'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Products'},
        ),
    ]
