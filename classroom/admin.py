from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Lesson, Chapter, Course

# Register your models here.
admin.site.register(Lesson, MarkdownxModelAdmin)
admin.site.register(Chapter)
admin.site.register(Course)
