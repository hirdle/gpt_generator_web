from rest_framework import serializers
from users.models import Channel, Image

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.themes = validated_data.get('themes', instance.themes)
        instance.save()
        return instance
    

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

    def delete(self, instance, validated_data):
        instance.delete()