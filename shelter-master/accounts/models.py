from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(
        max_length=50,
        verbose_name='이름',
        blank=True,
        null=True,
    )

    def get_full_name(self):
        return self.full_name

    def __str__(self):
        return self.full_name
