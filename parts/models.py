from django.db import models
from django.urls import reverse
from PIL import Image
from django.utils.text import slugify
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

from .utils import generate_unique_slug

# Create your models here.
class Product(models.Model):
    producer   = models.CharField(max_length=60)
    index       = models.TextField()
    description = models.TextField(blank=True, null=True)
    original       = models.TextField()
    instock     = models.IntegerField(blank=False)
    price       = models.DecimalField(decimal_places=2,max_digits=10000)
    


    def __str__(self):
        return self.index
        
class Category(MPTTModel):
    name   = models.CharField(max_length=200)
    slug   = models.SlugField(unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.ImageField(upload_to = 'images/%Y/%m/%d/%H/%M/%S/',)
    product = models.ForeignKey('Product',on_delete=models.CASCADE,related_name='odd_images')

    def __str__(self):
        return self.product.title