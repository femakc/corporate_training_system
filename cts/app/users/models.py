from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField
from posts.models import Course

from cts.settings import ROLES_CHOICES


class User(AbstractUser):
    phone = PhoneField(help_text='Номер телефона')
    fio = models.CharField(
        max_length=128,
        verbose_name="ФИО пользователя",
        help_text="ФИО"
    )
    role = models.CharField(
        max_length=32,
        choices=ROLES_CHOICES,
        default='user',
        verbose_name='Роль пользователя',
        help_text='роль'
    )
    user_group = models.ManyToManyField(
        Course,
        through="Enrollment",
        verbose_name="Курсы пользователя",
        help_text="Выберете курс"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['phone', 'fio'],
                                    name='phone_fio of constraint')
        ]

class Enrollment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='enroll'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enroll"
    )

    class Meta:
        verbose_name = 'Доступный курс'
        verbose_name_plural = 'Доступные курсы'
