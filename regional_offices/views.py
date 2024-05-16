from rest_framework import generics

from regional_offices.models import Event
from regional_offices.serializers import EventSerializer


class EventList(generics.ListAPIView):
    """Список событий."""

    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventRetrieve(generics.RetrieveAPIView):
    """Событие."""

    serializer_class = EventSerializer
    queryset = Event.objects.all()
