from rest_framework.serializers import ModelSerializer

from media_content.models import Image, Video


class ImageSerializer(ModelSerializer):
    """Serializer для модели Изображение."""

    class Meta:
        model = Image
        fields = ('image',)


class VideoSerializer(ModelSerializer):
    """Serializer для модели Видео."""

    class Meta:
        model = Video
        fields = ('video',)
