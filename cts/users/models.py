from cts.settings import ROLES_CHOICES
from django.db import models
from django.contrib.auth.models import AbstractUser
from posts.models import Course


class User(AbstractUser):
    role = models.CharField(
        max_length=32,
        choices=ROLES_CHOICES,
        default='user',
        verbose_name='Роль пользователя',
        help_text='роль'
    )
    user_group = models.ManyToManyField(Course, through="Enrollment")


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enroll')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enroll")
    date = models.DateField()
    mark = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Доступный курс'
        verbose_name_plural = 'Доступные курсы'
