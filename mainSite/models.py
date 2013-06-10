from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	price = models.IntegerField()
	def __unicode__(self):
		return u"%s" % self.product

class PageContent(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	def __unicode__(self):
		return u"%s" % self.pageContent

class ContactInfo(models.Model):
	name = models.CharField(max_length=200)
	addressLineOne = models.CharField(max_length=200)
	addressLineTwo = models.CharField(max_length=200)
	phoneOne = models.CharField(max_length=200)
	phoneTwo = models.CharField(max_length=200)
	fax = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	def __unicode__(self):
		return u"%s" % self.contactInfo
		
class SideBarContent(models.Model):
	rightItem = models.CharField(max_length=200)
	leftItem = models.CharField(max_length=200)
	def __unicode__(self):
		return u"%s" % self.sideBarContent