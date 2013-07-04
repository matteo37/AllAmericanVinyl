from django.db import models
from mezzanine.pages.models import Page
from django.contrib.auth.models import User

class About(Page):
    user = models.ManyToManyField(User)

class Products(Page):
    picture = models.FileField(upload_to='static/')
    name = models.TextField()
    height = models.DecimalField(decimal_places=2,max_digits=7)
    length = models.DecimalField(decimal_places=2,max_digits=7)

class Contact(Page):
    address = models.TextField()

# Create your models here.
