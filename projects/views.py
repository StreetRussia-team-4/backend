from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ReadOnlyModelViewSet

from projects.filters import ProjectFilter
from projects.models import Project
from projects.serializers import ProjectSerializer


@extend_schema(tags=['projects'])
@extend_schema_view(
    list=extend_schema(description='Получение списка проектов'),
    retrieve=extend_schema(description='Полная информация о проекте'),
)
class ProjectReadViewSet(ReadOnlyModelViewSet):
    """Проекты."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('region', 'current_status',)
    filterset_class = ProjectFilter
