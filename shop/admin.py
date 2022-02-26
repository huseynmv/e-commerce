from django.contrib import admin
from . models import Product, Order, OrderItem, ProductCategory
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('category', 'desc', 'name', 'price', 'image','size',)
    
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    fileds = ('name',)

admin.site.register(Order)
admin.site.register(OrderItem)


