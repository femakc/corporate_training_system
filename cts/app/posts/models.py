from core.models import CreatedModel
from django.conf import settings
from django.db import models
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField


class Course(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        help_text='Заголовок сообщест'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Адрес для страницы с постами',
        help_text='Адрес сообщест'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание сообщест'
    )

    def __str__(self):
        return self.title

    def get_slug(self):
        return self.slug

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Post(CreatedModel):
    text = RichTextField(
        null=True,
        blank=True,
        verbose_name='Статья с редактором',
        help_text='Редактируйте статью как вам хочеться'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Автор статьи",
        help_text='Автор'
    )
    group = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name="Группа",
        help_text='Группа, к которой будет относиться статья'
    )
    video = EmbedVideoField(
        blank=True,
        verbose_name="Видео",
        help_text="вставте ссылку на видео"
    )
    submit_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="LessonSubmitUser",
        verbose_name="урок пройден",
        help_text="пользователь прошел урок"
    )

    def __str__(self):
        return self.text[:15]

    class Meta:
        ordering = ['-created']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class LessonSubmitUser(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='lesson_submit'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="lesson_submit"
    )


class Comment(CreatedModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='comments',
        verbose_name="Пост",
        help_text='Пост к которому относится коментарий'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Автор поста",
        help_text='Автор'
    )
    text = models.TextField(
        verbose_name="Комментарий",
        help_text='Текст комментария'
    )

    def __str__(self):
        return "Комментарий"

    class Meta:
        ordering = ['-created']
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
