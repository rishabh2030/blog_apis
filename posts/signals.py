from django.conf import settings
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=BlogPost)
def create_lead_creation(sender, instance, created, **kwargs):
    print("working singlas")
    if created:
        if not instance.blog_id:
            instance.blog_id = "BLOG" + str(instance.id + (10 ** 2))
            instance.save()