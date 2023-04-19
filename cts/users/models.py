from cts.settings import ROLES_CHOICES
from django.db import models
from django.contrib.auth.models import AbstractUser
from posts.models import Course
from phonenumber_field.phonenumber import PhoneNumber
from phone_field import PhoneField
from psqlextra.indexes import UniqueIndex


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
    # date = models.DateField()
    # mark = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Доступный курс'
        verbose_name_plural = 'Доступные курсы'
