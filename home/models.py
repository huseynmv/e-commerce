from django.db import models

# Create your models here.

class HomeSlider(models.Model):
    image = models.ImageField(upload_to='home/slider/')
    title = models.CharField(max_length=200, null=True,blank=True)
    desc = models.CharField(max_length=200,null=True, blank=True)