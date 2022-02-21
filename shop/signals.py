from django.db.models.signals import post_save
from django.dispatch import receiver
from . models import Product
from django.template.defaultfilters import slugify

@receiver(post_save, sender=Product)
def save_shop(sender, created, instance, **kwargs):
    if created:
        instance.slug = slugify(instance.name + "-" + str(instance.created_at))
        instance.save()