from django.urls import include, path
from rest_framework.routers import DefaultRouter

from regional_offices.views import EventReadViewSet, SpotReadViewSet

v1_router = DefaultRouter()
v1_router.register(r'events', EventReadViewSet, basename='events')
v1_router.register(r'spots', SpotReadViewSet, basename='spots')

urlpatterns = [
    path('', include(v1_router.urls)),
]
