from django.db import models

from account.models import User

# Create your models here.

class Product(models.Model):
    category = models.CharField(max_length=127, null=True, blank=True)
    name = models.CharField(max_length=127, null=True, blank=True)
    price = models.SmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='shop/')
    
    
    class Meta:
        ordering = ('created_at',)
        
    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=255, null=True)