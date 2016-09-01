from django.contrib import admin
from .models import Lesson, Chapter, Course

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Chapter)
admin.site.register(Course)