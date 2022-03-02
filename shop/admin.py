from django.contrib import admin
from . models import Product, Order, OrderItem, ProductCategory, Color, Brand, Wishlist, WishlistItem
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
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
admin.site.register(OrderItem)


