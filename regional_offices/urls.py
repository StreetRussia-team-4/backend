from django.urls import path

from regional_offices.views import EventList, EventRetrieve

urlpatterns = [
    path('events/', EventList.as_view(), name='event_list'),
    path('events/<int:pk>', EventRetrieve.as_view(), name='event_detail'),
]
