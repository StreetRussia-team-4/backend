import django_filters
from django.utils import timezone

from projects.models import Project
from regional_offices.models import Region


class ProjectFilter(django_filters.FilterSet):
    """Фильтр для проектов"""

    region = django_filters.ModelChoiceFilter(
        queryset=Region.objects.all(),
        empty_label='Все регионы'
    )
    current_status = django_filters.ChoiceFilter(
        label='Статус',
        choices=Project.STATUS,
        method='filter_by_current_status',
    )

    class Meta:
        model = Project
        fields = ('region',)

    def filter_by_current_status(self, queryset, name, value):
        if value in (self.Meta.model.CURRENT, self.Meta.model.FUTURE):
            today = timezone.now().date()
            if value == self.Meta.model.CURRENT:
                queryset = queryset.filter(
                    is_finished=False,
                    start_date__lte=today,
                    end_date__gte=today
                )
            else:
                queryset = queryset.filter(
                    is_finished=False,
                    start_date__gt=today
                )
            return queryset
        queryset = queryset.filter(is_finished=True)
        return queryset
