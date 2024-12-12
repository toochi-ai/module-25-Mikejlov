from django import forms
from pydantic import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title_article_news',
            'text_article_news',
            'category',
            'author',
        ]
        labels = {
            'title_article_news': 'Заголовок',
            'text_article_news': 'Содержание',
            'category': 'Категория',
            'author': 'Автор',
        }

        def clean(self):
            cleaned_data = super().clean()
            title_article_news = cleaned_data.get("title_article_news")
            text_article_news = cleaned_data.get("text_article_news")

            if title_article_news == text_article_news:
                raise ValidationError(
                    "Описание не должно быть идентичным названию."
                )

            return cleaned_data
