from django.db import models
import random
import os
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.urls import reverse
from django.db.models import Q


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    new_file_name = random.randint(1,3422132133)
    name,ext = get_filename_ext(filename)
    final_name ='{}.{}'.format(new_file_name,ext)
    return 'products/{}/{}'.format(new_file_name,final_name)

class ProductQuerySet(models.query.QuerySet):

    def featured(self):
        return self.filter(featured=True, active=True)

    def active(self):
        return self.filter(active=True)

    def search(self,query):
        lookups = (Q(title__icontains=query) |
                   Q(description__icontains=query) |
                   Q(tag__title__icontains=query))
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):

    def all(self):
        return self.get_queryset().active()

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self,query):
        return self.get_queryset().active().search(query)

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=8,default=39.99)
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    slug = models.SlugField(blank=True,unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug":self.slug})


def product_pre_save_reciver(sender, instance, *args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciver, sender=Product)