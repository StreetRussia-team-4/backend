from rest_framework.serializers import ModelSerializer

from about.serializers import PartnerShortSerializer, PartnerSerializer
from projects.models import Project
from regional_offices.serializers import RegionSerializer


class ProjectSerializer(ModelSerializer):
    """Serializer для списка событий."""

    region = RegionSerializer(read_only=True)
    partners = PartnerSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "status",
            "name",
            "description",
            "region",
            "partners",
            "preview",
            "start_date",
            "end_date",
            "funds_raised",
            "goal",
        )
