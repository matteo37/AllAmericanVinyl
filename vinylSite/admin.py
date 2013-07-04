from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from vinylSite.models import Contact, Products, About

admin.site.register(Contact, PageAdmin)
admin.site.register(Products, PageAdmin)
admin.site.register(About, PageAdmin)
