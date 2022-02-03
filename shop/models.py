from django.db import models

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