from django import forms
from .models import Channel

class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ['name', 'telegram_id', 'themes', 'template', 'publish_interval']
        labels = {
            'name': 'Имя канала',
            'telegram_id': 'ID телеграм канала',
            'themes': 'Список тем (каждая с новой строки)',
            'template': 'Шаблон поста (обозначение темы - *Theme*)',
            'publish_interval': 'Интервал публикации (в минутах)',
        }