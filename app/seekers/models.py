from django.db import models
from insight.models import AbstractBaseModel
from seekers.tasks import initiate_run


class Seeker(AbstractBaseModel):
    SEEKER_PROTOTYPES = {
        'TEST': 'test'
    }
    PROTOTYPE_CHOICES = (
        (SEEKER_PROTOTYPES['TEST'], 'Test'),
    )
    prototype = models.CharField(
        'prototype', help_text='This seeker instance will be based on the selected Prototype',
        choices=PROTOTYPE_CHOICES, max_length=100
    )
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

    name = models.CharField('name', max_length=150, blank=True)
    seeker = models.ForeignKey(Seeker, on_delete=models.PROTECT)
    start = models.DateTimeField('run start', blank=True, null=True)
    end = models.DateTimeField('run end', blank=True, null=True)
    status = models.CharField('status', max_length=100, choices=STATUS_CHOICES, default=STATUSES['QUEUED'])
    logs = models.TextField('logs', blank=True)
    
    class Meta:
        verbose_name = 'run'
        verbose_name_plural = 'runs'
        ordering = ('-created', )


class Event(AbstractBaseModel):
    run = models.ForeignKey(Run, on_delete=models.CASCADE, related_name='events')
    timestamp = models.PositiveBigIntegerField('timestamp', db_index=True)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'
        ordering = ('timestamp', )


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


def run_post_save(sender, instance, created, **kwargs):
    if created:
        initiate_run.delay({ 'run_id': instance.id })

models.signals.post_save.connect(receiver=run_post_save)
