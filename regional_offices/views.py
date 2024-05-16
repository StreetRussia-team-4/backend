from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter

from regional_offices.models import Event
from regional_offices.serializers.event import EventSerializer


class BaseEvent:
    """Базовый класс событий."""
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventList(BaseEvent, generics.ListAPIView):
    """Список событий."""
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('name', 'description')
    search_fields = ('name', 'description')


class EventRetrieve(BaseEvent, generics.RetrieveAPIView):
    """Событие."""
    pass
