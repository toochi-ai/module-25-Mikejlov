# Generated by Django 5.1.2 on 2024-10-27 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_post_rating_article_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='user_rating',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='rating_comment',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='rating_article_news',
            new_name='rating',
        ),
    ]
