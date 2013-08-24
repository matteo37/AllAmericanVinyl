from django.db import models
from mezzanine.pages.models import Page
from django.contrib.auth.models import User


class About(Page):
    user = models.ManyToManyField(User)

class Services(Page):
    pass

class Products(Page):
    pass

class Contact(Page):
    address = models.TextField()
    email_to = models.EmailField()

class Product(models.Model):
    product = models.ForeignKey(Products)
    name = models.TextField()
    height = models.DecimalField(decimal_places=2,max_digits=7)
    length = models.DecimalField(decimal_places=2,max_digits=7)
    picture = models.ImageField(upload_to='products',null=True)
# Create your models here.
