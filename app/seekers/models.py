from django.db import models
from insight.models import AbstractBaseModel


class Seeker(AbstractBaseModel):
    name = models.CharField('name', max_length=255)
    description = models.TextField('description', blank=True)

    class Meta:
        verbose_name = 'seeker'
        verbose_name_plural = 'seekers'


class Run(AbstractBaseModel):
    STATUSES = {
        'QUEUED': 'queued',
        'IN_PROGRESS': 'in_progress',
        'COMPLETED': 'completed',
        'FAILED': 'failed'
    }
    STATUS_CHOICES = (
        (STATUSES['QUEUED'], 'Queued'),
        (STATUSES['IN_PROGRESS'], 'In progress'),
        (STATUSES['COMPLETED'], 'Completed'),
        (STATUSES['FAILED'], 'Failed'),
    )

    seeker = models.ForeignKey(Seeker, on_delete=models.PROTECT)
    start = models.DateTimeField('run start', blank=True, null=True)
    end = models.DateTimeField('run end', blank=True, null=True)
    status = models.CharField('status', max_length=100, choices=STATUS_CHOICES, default=STATUSES['QUEUED'])
    logs = models.TextField('logs', blank=True)
    
    class Meta:
        verbose_name = 'run'
        verbose_name_plural = 'runs'


class Training(AbstractBaseModel):
    STATUSES = {
        'QUEUED': 'queued',
        'IN_PROGRESS': 'in_progress',
        'COMPLETED': 'completed',
        'FAILED': 'failed'
    }
    STATUS_CHOICES = (
        (STATUSES['QUEUED'], 'Queued'),
        (STATUSES['IN_PROGRESS'], 'In progress'),
        (STATUSES['COMPLETED'], 'Completed'),
        (STATUSES['FAILED'], 'Failed'),
    )
    seeker = models.ForeignKey(Seeker, on_delete=models.PROTECT)
    start = models.DateTimeField('run start', blank=True, null=True)
    end = models.DateTimeField('run end', blank=True, null=True)
    status = models.CharField('status', max_length=100, choices=STATUS_CHOICES, default=STATUSES['QUEUED'])
    logs = models.TextField('logs', blank=True)
    
    class Meta:
        verbose_name = 'training'
        verbose_name_plural = 'trainings'
