from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from media_content.models import Image, Video


class ImageSerializer(ModelSerializer):
    """Serializer для модели Изображение."""
    link = serializers.ImageField(source='image')

    class Meta:
        model = Image
        fields = ('id', 'link',)


class VideoSerializer(ModelSerializer):
    """Serializer для модели Видео."""

    link = serializers.ImageField(source='video')

    class Meta:
        model = Video
        fields = ('id', 'link',)
