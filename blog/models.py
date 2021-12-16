from django.db import models

# Create your models here.
class Blog(models.Model):
    category = models.CharField(max_length=127, blank=True, null=True)
    name = models.CharField(max_length=127, blank=True, null=True)
    image = models.ImageField(upload_to='blog/')
    author = models.CharField(max_length=127, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    link = models.URLField(max_length=255)
    
    
    def __str__(self):
        return f'{self.name}'