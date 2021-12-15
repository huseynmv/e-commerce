from django.db import models

# Create your models here.

class Leaders(models.Model):
    image = models.ImageField(upload_to='leaders/')
    name = models.CharField(max_length=127)
    title = models.CharField(max_length=127)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Leader'
        
    def __str__(self):
        return f'{self.name}'