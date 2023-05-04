from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Channel
# from .tasks import create_schedule_task  


# @receiver(post_save, sender=Channel)
# def handle_table_update(sender, instance, **kwargs):
#     create_schedule_task(instance)  