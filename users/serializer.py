from rest_framework import serializers
from .models import Channel

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.themes = validated_data.get('themes', instance.themes)
        instance.save()
        return instance