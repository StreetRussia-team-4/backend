from rest_framework.serializers import ModelSerializer

from employees.models import RegionalManager


class RegionalManagerSerializer(ModelSerializer):
    """Serializer для модели Региональный руководитель."""

    class Meta:
        model = RegionalManager
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'tel',
            'vk_page',
            'photo',
        )
