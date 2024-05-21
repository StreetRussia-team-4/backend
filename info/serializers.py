from rest_framework.serializers import ModelSerializer

from info.models import Discipline


class DisciplineShortSerializer(ModelSerializer):
    """Serializer для модели Дисциплина."""

    class Meta:
        model = Discipline
        fields = ('id', 'name',)
