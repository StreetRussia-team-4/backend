from rest_framework.serializers import ModelSerializer

from about.serializers import PartnerShortSerializer
from info.serializers import DisciplineShortSerializer
from regional_offices.models import Event, Region


class RegionSerializer(ModelSerializer):
    """Serializer для модели Региона."""

    class Meta:
        model = Region
        fields = '__all__'


class EventShortSerializer(ModelSerializer):
    """Serializer для списка событий."""

    region = RegionSerializer(read_only=True)
    disciplines = DisciplineShortSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = (
            "name", "description", "date", "region", "disciplines", "preview",
        )


class EventFullSerializer(EventShortSerializer):
    """Serializer для модели События."""

    partners = PartnerShortSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = (
            "name", "description", "date", "region", "disciplines", "preview",
            "video", "website", "partners",
        )
