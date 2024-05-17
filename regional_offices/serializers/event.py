from rest_framework.serializers import ModelSerializer

from info.serializers import DisciplineSerializer
from media_content.serializers import ImageSerializer, VideoSerializer
from regional_offices.models import Event
from regional_offices.serializers.partners import PartnerSerializer
from regional_offices.serializers.region import RegionSerializer


class EventListSerializer(ModelSerializer):
    """Serializer для списка событий."""

    region = RegionSerializer(read_only=True)
    # partners = PartnerSerializer(many=True, read_only=True)
    # employee = RegionalManagerSerializer(read_only=True)
    disciplines = DisciplineSerializer(many=True, read_only=True)
    gallery = ImageSerializer(many=True, read_only=True)
    video = VideoSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            "name",
            "description",
            "date",
            # "website",
            "region",
            # "employee",
            "disciplines",
            # "partners",
            "gallery",
            "video",
        )


class EventRetrieveSerializer(ModelSerializer):
    """Serializer для модели События."""

    region = RegionSerializer(read_only=True)
    partners = PartnerSerializer(many=True, read_only=True)
    # employee = RegionalManagerSerializer(read_only=True)
    disciplines = DisciplineSerializer(many=True, read_only=True)
    gallery = ImageSerializer(many=True, read_only=True)
    video = VideoSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            "name",
            "description",
            "date",
            "website",
            "region",
            "employee",
            "disciplines",
            "partners",
            "gallery",
            "video",
        )
