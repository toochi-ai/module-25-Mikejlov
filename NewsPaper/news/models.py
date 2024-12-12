from django.contrib.auth.models import User
from django.db import models
from .resources import POSITIONS, news
from django.urls import reverse


class Author(models.Model):
    # связь «один к одному» со встроенной моделью пользователей User;
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)  # рейтинг пользователя.

    def update_rating(self):
        # суммарный рейтинг каждой статьи автора умножается на 3;
        post_rating = sum(post.rating * 3 for post in self.post_set.all())

        # суммарный рейтинг всех комментариев автора;
        comment_rating = sum(comment.rating * 3 for comment in self.user.comment_set.all())

        # суммарный рейтинг всех комментариев к статьям автора.
        post_comment_rating = sum(comment.rating for post in self.post_set.all() for comment in post.comment_set.all())

        # Итоговый рейтинг
        self.rating = post_rating + comment_rating + post_comment_rating
        self.save()


class Category(models.Model):
    # Категории новостей/статей. Имеет единственное поле: название категории. Поле должно быть уникальным
    # (в определении поля необходимо написать параметр unique = True).
    name_category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name_category.title()


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Author

    #  поле с выбором — «статья» или «новость»
    categoryType = models.CharField(max_length=2, choices=POSITIONS, default=news)
    time_in = models.DateTimeField(auto_now_add=True)  # автоматически добавляемая дата и время создания

    # связь «многие ко многим» с моделью Category(с дополнительной моделью PostCategory);
    category = models.ManyToManyField(Category, through='PostCategory')
    title_article_news = models.TextField(max_length=255)  # заголовок статьи / новости;
    text_article_news = models.TextField(null=True)  # текст статьи / новости;
    rating = models.IntegerField(default=0)  # рейтинг статьи / новости.

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text_article_news[0:123] + '...'

    def __str__(self):
        return f'{self.title_article_news.title()}: {self.text_article_news}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Post
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Category


class Comment(models.Model):
    # Под каждой новостью/статьёй можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.
    # Модель будет иметь следующие поля:
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Post;
    # связь «один ко многим» со встроенной моделью User (комментарии может оставить любой пользователь, необязательно автор)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField(max_length=255)  # текст комментария;
    time_in = models.DateTimeField(auto_now_add=True)  # дата и время создания комментария;
    rating = models.IntegerField(default=0)  # рейтинг комментария.

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
