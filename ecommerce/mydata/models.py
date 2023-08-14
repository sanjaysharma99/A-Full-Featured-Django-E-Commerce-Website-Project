from django.db import models
from .others import categories
from django.utils.translation import gettext


class Categories(models.Model):
    category_name=models.CharField(max_length=100)
    category_image=models.ImageField(upload_to='static/category_images/')
    category_slug=models.SlugField(unique=True)

    class Meta:
        verbose_name_plural=gettext('Categories')

obj1=categories()
category=obj1.getlist()

# Create your models here.
class Products(models.Model):
    product_name=models.CharField(max_length=100)
    product_slug=models.SlugField(unique=True)
    product_pric=models.IntegerField(default=0)
    product_category=models.CharField(max_length=10,choices=category)
    product_description=models.TextField(max_length=400)
    product_image=models.ImageField(upload_to='static/products_images/')

    class Meta:
        verbose_name_plural=gettext('Products')

class Carts(models.Model):
    cart_username=models.CharField(max_length=50)
    cart_product_name=models.CharField(max_length=200)
    cart_product_qty=models.IntegerField(default=0)

    class Meta:
        verbose_name_plural=gettext('Carts')
