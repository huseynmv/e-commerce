from django.contrib import admin
from . models import Product, Order, OrderItem, ProductCategory, Color, Brand, Wishlist, WishlistItem, Checkout
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('category','brand', 'price', 'image','image2','image3','image4','image5','size','color', 'name_az','name_en','desc_en', 'desc_az')
    
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    fileds = ('name',)

admin.site.register(Order)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
admin.site.register(OrderItem)
admin.site.register(Checkout)



