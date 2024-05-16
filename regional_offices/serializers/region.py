from rest_framework.serializers import ModelSerializer

from regional_offices.models import Event, Region


class RegionSerializer(ModelSerializer):
    """Serializer для модели Региона."""

    class Meta:
        model = Region
        fields = '__all__'
