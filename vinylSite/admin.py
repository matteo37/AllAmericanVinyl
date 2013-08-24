from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from vinylSite.models import Services, Contact, Products, About, Product

'''
page_fieldsets = deepcopy(PageAdmin.fieldsets)
page_fieldsets[0][1]["fields"].insert(-2, "products")
'''
extra_fieldsets = ((None, {"fields": ("something",)}),)

class ProductsInline(admin.TabularInline):
    model = Product

class MyPageAdmin(PageAdmin):
    inlines = (ProductsInline,)
    fieldsets = deepcopy(PageAdmin.fieldsets) #+ extra_fieldsets


admin.site.register(Contact, PageAdmin)
admin.site.register(Services, PageAdmin)
admin.site.register(Products, MyPageAdmin)
admin.site.register(About, PageAdmin)
admin.site.register(Product)
