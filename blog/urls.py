from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.views import BlogViewSet

v1_router = DefaultRouter()
v1_router.register('', BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(v1_router.urls)),
]
