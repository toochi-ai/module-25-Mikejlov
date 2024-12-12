from django.urls import path
# Импортируем созданные нами представления
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, PostSearch

urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', PostsList.as_view() ),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('news/create/', PostCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_filter'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('articles/create/', PostCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_filter'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),

]
