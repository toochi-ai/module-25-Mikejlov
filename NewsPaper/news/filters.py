import django_filters
from django.forms import DateInput
from django_filters import FilterSet, ModelChoiceFilter
from .models import Post, User


# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    title_article_news = django_filters.CharFilter(lookup_expr='icontains', label='Заголовок')
    time_in = django_filters.DateFilter(field_name='time_in', lookup_expr='gte', label='Опубликовано после',
                                        widget=DateInput(attrs={'type': 'date'}))
    author = ModelChoiceFilter(
        field_name='author__user__username',
        empty_label='Любой',
        queryset=User.objects.all(),
        label='Автор'
    )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = [
            # поиск по названию
            'title_article_news',
            # по имени автора
            'author',
            # позже указываемой даты
            'time_in'
        ]
