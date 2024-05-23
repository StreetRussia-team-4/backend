from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from blog.models import Post
from blog.permissions import IsAuthorOrReadOnly
from blog.serializers import PostListSerializer, PostDetailSerializer


@extend_schema(tags=['posts'])
@extend_schema_view(
    list=extend_schema(description='Получение списка записей блога'),
    retrieve=extend_schema(description='Полная информация о записи блога'),
)
class BlogViewSet(ModelViewSet):
    """Записи блога."""

    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)
    serializer_class = PostDetailSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('type', 'author',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return self.serializer_class
