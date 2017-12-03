from django.db import models
import random
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    new_file_name = random.randint(1,3422132133)
    name,ext = get_filename_ext(filename)
    final_name ='{}.{}'.format(new_file_name,ext)
    return 'products/{}/{}'.format(new_file_name,final_name)

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=8,default=39.99)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title