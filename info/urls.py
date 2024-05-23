from django.urls import path, include
from rest_framework.routers import DefaultRouter

from info.views import (NewsViewSet, FilmViewSet, InterviewViewSet,
                        ArticleViewSet)

v1_info_router = DefaultRouter()
v1_info_router.register('articles', ArticleViewSet, basename='articles')
v1_info_router.register('interviews', InterviewViewSet, basename='interviews')
v1_info_router.register('films', FilmViewSet, basename='films')
v1_info_router.register('news', NewsViewSet, basename='news')

urlpatterns = [
    path('', include(v1_info_router.urls)),
]
