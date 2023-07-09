from django import forms
from .models import Channel, Image

class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ['name', 'telegram_id', 'site_link', 'vk_id', 'themes', 'template', 'publish_interval', 'overlay']
        labels = {
            'name': 'Имя канала',
            'telegram_id': 'ID телеграм канала',
            'vk_id': 'ID ВК группы',
            'site_link': 'Ссылка на сайт с HTTPS',
            'themes': 'Список тем (каждая с новой строки)',
            'template': 'Шаблон поста (обозначение темы - *Theme*)',
            'publish_interval': 'Расписание публикаций (пример: 13:00, 15:00, каждое время с новой строки)',
            'overlay': 'Картинка для наложения на фото при публикации',
        }



class ImageForm(forms.ModelForm):

    theme_id = forms.IntegerField(min_value=1, label="ID темы к которой будет привязана картинка*", required=True)

    class Meta:
        model = Image
        fields = ['theme', 'upload', 'owner', 'channel']
        labels = {
            'upload': 'Картинка',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner'].required = False
        self.fields['channel'].required = False
        self.fields['theme'].required = False