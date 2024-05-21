from django.urls import include, path
from rest_framework.routers import DefaultRouter

from regional_offices.views import EventReadViewSet

v1_events_router = DefaultRouter()
v1_events_router.register(r'events', EventReadViewSet, basename='news')


urlpatterns = [
    path('', include(v1_events_router.urls)),
]
