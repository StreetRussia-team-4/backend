from rest_framework.serializers import ModelSerializer

from about.serializers import PartnerShortSerializer
from employees.serializers import RegionalManagerSerializer
from info.serializers import DisciplineShortSerializer
from media_content.serializers import ImageSerializer, VideoSerializer
from regional_offices.models import City, Event, Region, Spot


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
    employee = RegionalManagerSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            "name", "description", "date", "region", "disciplines", "preview",
            "video", "website", "partners", 'employee',
        )


class CitySerializer(EventShortSerializer):
    """Serializer для модели City."""
    region = RegionSerializer(read_only=True)

    class Meta:
        model = City
        fields = (
            "id",
            "name",
            "region",
        )


class SpotSerializer(EventShortSerializer):
    """Serializer для модели Локация."""
    city = CitySerializer(read_only=True)
    gallery = ImageSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Spot
        fields = (
            "id",
            "name",
            "city",
            "name",
            "spot_type",
            "address",
            "website",
            "gallery",
            "videos",
            "coordinates"
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['spot_type'] = {
            "value": instance.spot_type,
            "description": dict(self.Meta.model.TYPES)[instance.spot_type]
        }
        region = representation['city'].pop('region')
        representation['region'] = region
        return representation
