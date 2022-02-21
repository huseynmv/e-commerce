from django.contrib import admin
from . models import Product, Order, OrderItem, ProductCategory
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('category', 'desc', 'name', 'price', 'image',)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ProductCategory)
