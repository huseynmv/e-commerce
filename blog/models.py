from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=127, null=True, blank=True)

class Blog(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, max_length=127, blank=True, null=True)
    name = models.CharField(max_length=127, blank=True, null=True)
    image = models.ImageField(upload_to='blog/')
    author = models.CharField(max_length=127, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    desc = RichTextField(help_text='Content', null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.name}'
    
