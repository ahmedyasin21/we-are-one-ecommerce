from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from src.utils import profile_unique_slug_generator
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _
from categories.models import ShopCategory
# from django.utils.text import slugify
# Create your models here.



# class ShopProfileManager(models.Manager):



#     def get_queryset(self):
#         return super().get_queryset().filter()






class ShopProfile(models.Model):



    shop_owner = models.OneToOneField(User, related_name='shop_profile', on_delete=models.CASCADE)
    shop_address = models.CharField(_("shop address"), max_length=255)
    title = models.CharField(("Shop Title"), max_length=50)
    shop_url = models.URLField(_("Shop Url"), max_length=200,null=True,blank=True)
    slug = models.SlugField(blank =True,unique = True)
    tag_line = models.CharField(_("Tag Line"),default="We are one." , max_length=100, null=True, blank=True)
    city = models.CharField(("city"), max_length=50,null=True,blank=True)
    create_date = models.DateTimeField(("create date"), default=timezone.now)
    shop_category = models.CharField(("shop catagory"), max_length=150,blank=True)
    # shop_category = models.ForeignKey(ShopCategory, verbose_name=_("shop category"), on_delete=models.CASCADE,blank=True,null=True)
    shop_bg  =models.ImageField(_("Shop Logo"), upload_to="shop_back_grounds",default="shop_default.jpeg" ,height_field=None, width_field=None, max_length=None)
    customers = models.ManyToManyField(User, related_name="customers", verbose_name=_("coutomers"),blank=True)
    customers_favorite = models.ManyToManyField(User,related_name="customers_favorite", verbose_name=_("customers favorite"),blank=True)
    description = models.CharField(("shop description"), max_length=350, default="I'm glad you're visiting our shop!",null=True,blank=True)


    # social links

    facebook = models.URLField(("facebook"), max_length=200,null=True,blank=True)
    twitter = models.URLField(("twitter"), max_length=200,null=True,blank=True)
    pinterest = models.URLField(("pinterest"), max_length=200,null=True,blank=True)
    instagram = models.URLField(("instagram"), max_length=200,null=True,blank=True)
    youtube = models.URLField(("youtube"), max_length=200,null=True,blank=True)
    daraz = models.URLField(("daraz"), max_length=200,null=True,blank=True)
    amazon = models.URLField(("amazon"), max_length=200,null=True,blank=True)

    def __str__(self):
        return self.shop_owner.username
    
    # def save(self,*args,**kwargs):
    #     self.slug=slugify(self.title)
    #     super(ShopProfile,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("shops:shop_profile_update", kwargs={"slug": self.slug})

def shopprofile_pre_save_reciever(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = profile_unique_slug_generator(instance)
    else:
        instance.slug = profile_unique_slug_generator(instance)
pre_save.connect(shopprofile_pre_save_reciever,ShopProfile)


