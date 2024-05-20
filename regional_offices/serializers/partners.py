from rest_framework.serializers import ModelSerializer

from about.models import Partner


class PartnerSerializer(ModelSerializer):
    """Serializer для модели Партнеры."""

    class Meta:
        model = Partner
        fields = '__all__'
