from rest_framework.serializers import ModelSerializer

from about.models import Partner


class PartnerShortSerializer(ModelSerializer):
    """Serializer для модели Партнер."""

    class Meta:
        model = Partner
        fields = ('id', 'logo',)
