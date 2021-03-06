from django.db import models
from account.models import User
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=127, null=True, blank=True)
    slug = models.SlugField(max_length=127, null=True, blank=True)
    
    def __str__(self):
        return self.name
    


class Blog(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, max_length=127, blank=True, null=True)
    tags = TaggableManager()
    name = models.CharField(max_length=127, blank=True, null=True)
    image = models.ImageField(upload_to='blog/')
    author = models.CharField(max_length=127, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    desc = RichTextField(help_text='Content', null=True, blank=True)
    slug = models.SlugField(max_length=127, null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.name}'
  
    class Meta:
        ordering = ['-id']
    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments', null=True, blank=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return (self.name)
