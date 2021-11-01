from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_countries.fields import CountryField
from django.utils import timezone
from categories.models import ShopCategory
from shops.models import ShopProfile
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class ShopRequest(models.Model):

    Gender = (
    ('male','Male'),
    ('female','Female'),
    ('others','Others'),
    )

    ID_proof = (
    ('1','Licence'),
    ('2','Government id'),
    ('3','Passport'),
    )

    Address_proof= (
    ('1','Licence'),
    ('2','Government id'),
    ('3','Passport'),
    )

    Approved = (
    ('Approved','Approved'),
    ('Cancel','Cancel'),
    )

    requested_user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(("first name"), max_length=50)
    last_name = models.CharField(("last name"), max_length=50)
    age = models.IntegerField(("age"))
    gender = models.CharField(("gender"), max_length=50,choices=Gender)
    nationality = models.CharField(("nationality"), max_length=50)
    country = CountryField()
    phone_number = PhoneNumberField()
    state = models.CharField(("state"), max_length=50)
    city = models.CharField(("city"), max_length=50)
    zip_code = models.CharField(("zip code"), max_length=50)
    street_address = models.CharField(("street address"), max_length=50)
    address_proof = models.CharField(("address proof"), max_length=50,choices=Address_proof)
    address_proof_img = models.ImageField(("Address Verification"), upload_to='address_proof_img', height_field=None, width_field=None, max_length=None)
    
    id_proof = models.CharField(("face verification"), max_length=50,choices=ID_proof)
    id_proof_img = models.ImageField(("ID Verification"), upload_to='id_proof_img', height_field=None, width_field=None, max_length=None)
    shop_title = models.CharField(("Shop title"), max_length=75)
    shop_category = models.ForeignKey(ShopCategory, verbose_name=("shop category"), on_delete=models.CASCADE)
    shop_address = models.CharField(("shop address"), max_length=75)
    request_approve = models.CharField(("request approval"), max_length=50,choices=Approved)
    create_date = models.DateTimeField(("create date"), default=timezone.now)


    
    def __str__(self):
        return self.requested_user.username

    def save(self,*args, **kwargs):
        response = "i'm updated"
        print(response)
        super(ShopRequest,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("shoprequests:shop_form_detail", kwargs={"pk": self.pk})
