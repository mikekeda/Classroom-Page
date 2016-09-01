from django.conf.urls import url

from .views import classroom, lesson

urlpatterns = [
    url(r'^$', classroom, name='index'),
    url(r'^lesson/(?P<lesson_id>\d+)', lesson, name='lesson')
]
