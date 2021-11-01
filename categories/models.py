from django.db import models
from django.urls import reverse
from src.utils import category_unique_slug_generator
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class ShopCategory(models.Model):

    
    name = models.CharField(("shop categories"), max_length=150)
    slug = models.SlugField(blank =True,unique = True)
    image = models.ImageField(("shop category image"), upload_to='shop_category', height_field=None, width_field=None, max_length=None,blank=True,null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories:categories_detail", kwargs={"slug": self.slug})


def shopcategory_pre_save_reciever(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = category_unique_slug_generator(instance)
pre_save.connect(shopcategory_pre_save_reciever,ShopCategory)

class PostCategory(models.Model):

    
    name = models.CharField(("post categories"), max_length=150)
    slug = models.SlugField(blank =True,unique = True)
    image = models.ImageField(("post category image"), upload_to='post_category', height_field=None, width_field=None, max_length=None,blank=True,null=True)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories:categories_detail", kwargs={"slug": self.slug})


def postcategory_pre_save_reciever(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = category_unique_slug_generator(instance)
pre_save.connect(postcategory_pre_save_reciever,PostCategory)