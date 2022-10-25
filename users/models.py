from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

from datetime import date
from dateutil.relativedelta import relativedelta

USER_MIN_AGE = 9


def birth_date_validator(value):
    diff_years = relativedelta(date.today(), value).years()
    if diff_years < USER_MIN_AGE:
        raise ValidationError("User is underage")
    return value


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'


class UserRoles:
    USER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = (
        ("Пользователь", USER),
        ("Админ", ADMIN),
        ("Модератор", MODERATOR),
    )


class User(AbstractUser):
    role = models.CharField(choices=UserRoles.choices, default='member', max_length=12)
    location = models.ManyToManyField(Location)
    age = models.PositiveSmallIntegerField(null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200)
    birth_date = models.DateField(validators=[birth_date_validator])
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



