from rest_framework.serializers import ModelSerializer

from info.models import Discipline


class DisciplineSerializer(ModelSerializer):
    """Serializer для модели Дисциплина."""

    class Meta:
        model = Discipline
        fields = '__all__'
