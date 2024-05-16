from rest_framework.serializers import ModelSerializer

from media_content.models import Image


class ImageSerializer(ModelSerializer):
    """Serializer для модели Изображение."""

    class Meta:
        model = Image
        fields = '__all__'


class VideoSerializer(ModelSerializer):
    """Serializer для модели Видео."""

    class Meta:
        model = Image
        fields = '__all__'
