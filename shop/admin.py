from django.contrib import admin
from . models import Product, Order, OrderItem, ProductCategory, Color, Brand
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('category', 'desc', 'name', 'price', 'image','size','color',)
    
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    fileds = ('name',)

admin.site.register(Order)
admin.site.register(Color)
admin.site.register(Brand)

admin.site.register(OrderItem)


