from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ReadOnlyModelViewSet

from regional_offices.models import Event
from regional_offices.serializers import (EventFullSerializer,
                                          EventShortSerializer)


@extend_schema(tags=['events'])
@extend_schema_view(
    list=extend_schema(description='Получение списка событий'),
    retrieve=extend_schema(description='Полная информация о конкретном событии'),
)
class EventReadViewSet(ReadOnlyModelViewSet):
    """Список событий."""

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('region', 'disciplines',)

    def get_queryset(self):
        if self.action == 'list':
            return Event.objects.all()
        return Event.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return EventShortSerializer
        return EventFullSerializer
