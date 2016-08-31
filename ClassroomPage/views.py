from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def landingPage(request):
	return render(request, 'landing.html')


def lessonView(request, lessonID):
	params = {}
	params['lessonID'] = lessonID
	return render(request, 'lesson.html', params)

def classroomView(request):
	return render(request, 'classroom.html')