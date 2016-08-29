from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def landingPage(request):
	return render(request, 'landing.html')


def lessonView(request):
	return render(request, 'lesson.html')
