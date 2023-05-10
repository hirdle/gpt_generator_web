from django.db import models 
import os
from django.contrib.auth.models import User

class Channel(models.Model):

    name = models.CharField(max_length=255, default="Default")
    telegram_id = models.IntegerField(null=True, blank=True)
    themes = models.TextField(default="", null=True, blank=True)
    template = models.TextField(default="*Theme*")
    publish_interval = models.TextField(default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)



def user_directory_path(instance, filename):
    return f'channels_images/{instance.channel.id}/' + filename


class Image(models.Model):

    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    upload = models.ImageField(upload_to=user_directory_path)
    theme = models.CharField(max_length=200, default="")


    def delete(self, using=None, keep_parents=False):
        os.remove(self.upload.path)
        super().delete(using=using, keep_parents=keep_parents)