from rest_framework.serializers import ModelSerializer

from about.models import Partner, PartnerType


class PartnerTypeSerializer(ModelSerializer):
    """Serializer для модели Тип Партнера."""
    class Meta:
        model = PartnerType
        fields = ('id', 'name',)


class PartnerShortSerializer(ModelSerializer):
    """Serializer для модели Партнер."""

    class Meta:
        model = Partner
        fields = ('id', 'logo',)


class PartnerSerializer(ModelSerializer):
    """Serializer для модели Партнер."""
    type = PartnerTypeSerializer(read_only=True)

    class Meta:
        model = Partner
        fields = ('id', 'name', 'type', 'logo', 'website')
