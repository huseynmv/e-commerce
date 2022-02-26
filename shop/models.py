from statistics import mode
from django.db import models

from account.models import User

# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=127, null=True, blank=True)
    
class Brand(models.Model):
    name = models.CharField(max_length=127, null=True, blank=True)

class ProductCategory(models.Model):
    name = models.CharField(max_length=127, null=True, blank=True)
    slug = models.SlugField(max_length=127, null=True, blank=True)

class Product(models.Model):
    color = models.ForeignKey(Color,on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brand,on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL,max_length=127, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=127, null=True, blank=True)
    price = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='shop/')
    slug = models.SlugField(max_length=127, null=True, blank=True)
    
    
    class Meta:
        ordering = ('created_at',)
    
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
 
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total