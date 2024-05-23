from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ReadOnlyModelViewSet

from info.models import News, Article, Interview, Film
from info.permissions import IsAuthorOrReadOnly
from info.serializers import (NewsSerializer, ArticleSerializer,
                              InterviewSerializer, FilmSerializer)


@extend_schema(tags=['posts'])
@extend_schema_view(
    list=extend_schema(description='Получение списка записей блога'),
    retrieve=extend_schema(description='Полная информация о записи блога'),
)
class BlogViewSet(ReadOnlyModelViewSet):
    """Записи блога."""

    model = Article
    queryset = model.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('discipline',)


@extend_schema_view(
    list=extend_schema(description='Получение списка статей'),
    retrieve=extend_schema(description='Статья'),
)
class ArticleViewSet(BlogViewSet):
    """Cтатьи."""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


@extend_schema_view(
    list=extend_schema(description='Получение списка интервью'),
    retrieve=extend_schema(description='Интервью'),
)
class InterviewViewSet(BlogViewSet):
    """Интервью."""

    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


@extend_schema_view(
    list=extend_schema(description='Получение списка фильмов'),
    retrieve=extend_schema(description='Фильм'),
)
class FilmViewSet(BlogViewSet):
    """Фильмы."""

    queryset = Film.objects.all()
    serializer_class = FilmSerializer


@extend_schema_view(
    list=extend_schema(description='Получение списка новостей'),
    retrieve=extend_schema(description='Полная новости'),
)
class NewsViewSet(BlogViewSet):
    """Записи новостей."""

    queryset = News.objects.all()
    serializer_class = NewsSerializer
