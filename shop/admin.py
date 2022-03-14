from django.contrib import admin
from math import ceil
from . models import Product, Order, OrderItem, ProductCategory, Color, Brand, Wishlist, WishlistItem, Checkout, Discount
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('category','brand', 'price', 'image','image2','image3','image4','image5','size','color', 'name_az','name_en','desc_en', 'desc_az')
    actions = ['discount_30']
    
    for i in list(Discount.objects.all().values_list('discount_price', flat=True)):
            print(i)
        # print(list(Discount.objects.all().values_list('discount_price', flat=True)))
            global discount
            discount = i  # percentage
            def discount_30(self,request, queryset):


                for product in queryset:
                    print(discount)
                    multiplier = discount / 100  
                    old_price = product.price
                    new_price = ceil(old_price - (old_price * multiplier))
                    product.price = new_price
                    product.save(update_fields=['price'])
            discount_30.short_description = f'Set {discount} discount'
        
    
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
admin.site.register(Discount)


