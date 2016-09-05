from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def landing_page(request):
    form = UserCreationForm()
    return render(request, 'landing.html', dict(form=form, user=request.user))
