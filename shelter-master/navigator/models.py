from django.db import models

from accounts.models import User


class Shelter(models.Model):
    name = models.CharField(
        verbose_name='이름',
        max_length=50,
    )
    lat = models.DecimalField(
        verbose_name='위도',
        max_digits=9,
        decimal_places=6,
    )
    lon = models.DecimalField(
        verbose_name='경도',
        max_digits=9,
        decimal_places=6,
    )

    class Meta:
        verbose_name = '쉼터'
        verbose_name_plural = '쉼터'

    def get_num_guardians(self):
        return len(self.guardians)

    get_num_guardians.short_description = '선생님의 수'

    def __str__(self):
        return self.name


class Guardian(User):
    shelter = models.ForeignKey(
        verbose_name='소속',
        to=Shelter,
        related_name='guardians',
        on_delete=models.CASCADE,
    )
    phone_number = models.CharField(
        verbose_name='전화번호',
        max_length=11,
    )

    class Meta:
        verbose_name = '선생님'
        verbose_name_plural = '선생님'


class Request(models.Model):
    WEB, IOS, ANDROID = 'W', 'I', 'A'
    PLATFORM_CHOICES = [
        (WEB, 'Web'),
        (IOS, 'iOS'),
        (ANDROID, 'Android'),
    ]

    time = models.DateTimeField(
        verbose_name='요청 시각',
        auto_now_add=True,
    )
    lat = models.DecimalField(
        verbose_name='위도',
        max_digits=9,
        decimal_places=6,
    )
    lon = models.DecimalField(
        verbose_name='경도',
        max_digits=9,
        decimal_places=6,
    )
    name = models.CharField(
        verbose_name='이름',
        max_length=50,
        blank=True,
    )
    phone_number = models.CharField(
        verbose_name='전화번호',
        max_length=11,
    )
    platform = models.CharField(
        verbose_name='플랫폼',
        max_length=1,
        choices=PLATFORM_CHOICES,
        default=WEB,
    )

    class Meta:
        verbose_name = '도움 요청'
        verbose_name_plural = '도움 요청'

    def get_location(self):
        return '({}, {})'.format(self.lat, self.lon)

    get_location.short_description = '위치'

    def __str__(self):
        return '도움 요청 #{}'.format(self.id)
