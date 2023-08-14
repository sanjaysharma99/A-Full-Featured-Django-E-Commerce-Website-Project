# Generated by Django 4.2.2 on 2023-07-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0004_rename_categorys_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='products',
            name='product_category',
            field=models.CharField(choices=[('Laptop', 'Laptop'), ('Smartphone', 'Smartphone'), ('Watches', 'Watches')], max_length=10),
        ),
    ]
