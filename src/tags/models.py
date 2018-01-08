from django.db import models
<<<<<<< HEAD
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from products.models import Product

from products.utils import unique_slug_generator
=======
from django.db.models.signals import pre_save
from products.utils import unique_slug_generator
from products.models import Product

>>>>>>> 91537c5eaa003beff4a98cefe8318e7918c86fa4
# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
<<<<<<< HEAD
    time_stamp = models.DateTimeField(auto_now_add=True)
=======
    timestamp = models.DateTimeField(auto_now_add=True)
>>>>>>> 91537c5eaa003beff4a98cefe8318e7918c86fa4
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title

def tag_pre_save_reciver(sender, instance, *args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(tag_pre_save_reciver, sender=Tag)