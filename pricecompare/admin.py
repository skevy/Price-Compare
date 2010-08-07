from django.contrib import admin
from pricecompare.models import *

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
    
class ProductGroupAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_group', 'source', 'price', 'got_price']

admin.site.register(Source)
admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(Product, ProductAdmin)