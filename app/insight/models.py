from django.db import models


class AbstractBaseModel(models.Model):
    created = models.DateTimeField('created', auto_now_add=True, db_index=True)
    modified = models.DateTimeField('modified', auto_now=True, db_index=True)

    class Meta:
        abstract = True
