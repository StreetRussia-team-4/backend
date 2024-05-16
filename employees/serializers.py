from rest_framework.serializers import ModelSerializer

from employees.models import RegionalManager


class RegionalManagerSerializer(ModelSerializer):
    """Serializer для модели Региональный руководитель."""

    class Meta:
        model = RegionalManager
        fields = '__all__'
