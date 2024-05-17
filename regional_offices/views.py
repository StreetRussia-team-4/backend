from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter

from info.models import Discipline
from media_content.models import Image
from regional_offices.models import Event
from regional_offices.serializers.event import EventListSerializer, \
    EventRetrieveSerializer


class BaseEvent:
    """Базовый класс событий."""

    queryset = (
        Event.objects
        .select_related("region", "employee", "video")
        .prefetch_related(
            # 'disciplines',
            Prefetch('disciplines', queryset=Discipline.objects.prefetch_related('videos').all()),
            "partners",
            Prefetch('gallery', queryset=Image.objects.all()),
            # "gallery"   
        )
        .all()
    )# TODO: оптимизировать запрос


class EventList(BaseEvent, generics.ListAPIView):
    """Список событий."""

    serializer_class = EventListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('name', 'description', "region__name", "date__date")
    search_fields = ('name', 'description', 'region__name__iregex')


class EventRetrieve(BaseEvent, generics.RetrieveAPIView):
    """Событие."""

    serializer_class = EventRetrieveSerializer
