from django.urls import path

from regional_offices import views

urlpatterns = [
    path('events/', views.EventList.as_view(), name='event_list'),
    path(
        'events/<int:pk>',
        views.EventRetrieve.as_view(),
        name='event_detail'
    ),
]
