from __future__ import unicode_literals

from django.db import models
from django.db.models.functions import Trunc


# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name

    @staticmethod
    def formatted_time(annotated_queryset):
        annotated_queryset = annotated_queryset.annotate(
            add_time_formatted=Trunc('add_time', 'second', output_field=models.DateTimeField())
        )
        return annotated_queryset
