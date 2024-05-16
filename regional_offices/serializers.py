from rest_framework.serializers import ModelSerializer

from regional_offices.models import Event


class EventSerializer(ModelSerializer):
    """Serializer для модели События"""

    class Meta:
        model = Event
        fields = '__all__'
