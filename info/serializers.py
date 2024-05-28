from rest_framework.serializers import ModelSerializer

from about.serializers import PartnerShortSerializer
from info.models import Article, Discipline, Film, Interview, News


class DisciplineShortSerializer(ModelSerializer):
    """Serializer для модели Дисциплина."""

    class Meta:
        model = Discipline
        fields = ('id', 'name',)


class BlogBaseSerializer(ModelSerializer):
    """Serializer для записи."""
    discipline = DisciplineShortSerializer(read_only=True)
    partner = PartnerShortSerializer(read_only=True)

    class Meta:
        fields = (
            "id",
            "name",
            "description",
            "pub_date",
            'source_link',
            "discipline",
            "partner",
            "preview",
        )


class ArticleSerializer(BlogBaseSerializer):
    """Serializer для статьи."""

    class Meta(BlogBaseSerializer.Meta):
        model = Article


class InterviewSerializer(BlogBaseSerializer):
    """Serializer для интервью."""

    class Meta(BlogBaseSerializer.Meta):
        model = Interview


class FilmSerializer(BlogBaseSerializer):
    """Serializer для фильма."""

    class Meta(BlogBaseSerializer.Meta):
        model = Film


class NewsSerializer(BlogBaseSerializer):
    """Serializer для новостей."""

    class Meta(BlogBaseSerializer.Meta):
        model = News
