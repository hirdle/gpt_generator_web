from django.db import models 
from django.contrib.auth.models import User

class Channel(models.Model):

    name = models.CharField(max_length=255, default="Default")
    telegram_id = models.IntegerField()
    themes = models.TextField(default="", null=True, blank=True)
    template = models.TextField(default="*Theme*")
    publish_interval = models.TextField(default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)