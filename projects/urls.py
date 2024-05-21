from django.urls import include, path
from rest_framework.routers import DefaultRouter

from projects.views import ProjectReadViewSet

v1_projects_router = DefaultRouter()
v1_projects_router.register('', ProjectReadViewSet, basename='projects')

urlpatterns = [
    path('', include(v1_projects_router.urls)),
]
