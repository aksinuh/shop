from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import detail
from django.utils.text import slugify
import random

@receiver(post_save, sender = detail)
def slug(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.title) + "-" +str(random.randint(10000, 999999))
        instance.save()