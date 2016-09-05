from __future__ import unicode_literals

from django.db import models
from markdownx.models import MarkdownxField


class Timestamp(models.Model):
    """Abstract model to get the created, updated fields in each model by default"""
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Lesson(Timestamp):
    """Lesson model"""
    title = models.CharField(max_length=250)
    content = MarkdownxField()

    def __unicode__(self):
        return str(self.id) + ' Lesson: ' + self.title


class Chapter(Timestamp):
    """Chapter model"""
    title = models.CharField(max_length=250)
    lessons = models.ManyToManyField(Lesson)

    def __unicode__(self):
        return str(self.id) + ' Chapter: ' + self.title


class Course(Timestamp):
    """Course model"""
    title = models.CharField(max_length=250)
    chapters = models.ManyToManyField(Chapter)

    def __unicode__(self):
        return str(self.id) + ' Course: ' + self.title
