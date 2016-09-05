from django.shortcuts import render, get_object_or_404


# Create your views here.
from classroom.models import Lesson


def lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)

    context = {
        'lesson': lesson
    }
    return render(request, 'lesson.html', context)


def classroom(request):
    return render(request, 'classroom.html')
