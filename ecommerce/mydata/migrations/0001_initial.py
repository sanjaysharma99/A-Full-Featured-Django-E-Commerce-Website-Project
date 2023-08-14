# Generated by Django 4.2.2 on 2023-07-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_username', models.CharField(max_length=50)),
                ('cart_product_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_slug', models.SlugField(unique=True)),
                ('product_pric', models.IntegerField(default=0)),
                ('product_category', models.CharField(choices=[('laptop', 'Laptop'), ('smartphone', 'Smartphone')], default='men', max_length=10)),
                ('product_description', models.TextField(max_length=400)),
                ('product_image', models.ImageField(upload_to='static/products/')),
            ],
        ),
    ]