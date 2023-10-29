from django.db import models
from insight.models import AbstractBaseModel


class Seeker(AbstractBaseModel):
    name = models.CharField('name', max_length=255)
    description = models.TextField('description', blank=True)

    class Meta:
        verbose_name = 'seeker'
        verbose_name_plural = 'seekers'
