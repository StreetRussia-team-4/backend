from rest_framework.serializers import ModelSerializer

from employees.models import RegionalManager
from info.serializers import DisciplineSerializer
from media_content.serializers import ImageSerializer


class RegionalManagerSerializer(ModelSerializer):
    """Serializer для модели Региональный руководитель."""
    photo = ImageSerializer(read_only=True)
    # discipline = DisciplineSerializer(read_only=True)

    class Meta:
        model = RegionalManager
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'photo',
            'discipline',
        )
