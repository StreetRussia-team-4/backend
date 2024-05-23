from rest_framework.serializers import ModelSerializer

from about.serializers import PartnerShortSerializer, PartnerSerializer
from blog.models import PostType, Post
from projects.models import Project
from regional_offices.serializers import RegionSerializer
from users.serializers import UserSerializer


class PostTypeSerializer(ModelSerializer):
    """Serializer для типа записи."""
    class Meta:
        model = PostType
        fields = (
            'id',
            'name',
            'description',
            'order',
        )


class PostListSerializer(ModelSerializer):
    """Serializer для списка записей."""

    type = PostTypeSerializer(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "type",
            "author",
            "preview",
        )


class PostDetailSerializer(PostListSerializer):
    """Serializer для записи."""

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "type",
            "author",
            "preview",
            "text"
        )
