from django.contrib.auth.models import auth
from django.shortcuts import redirect


def login(request):
    """Login form."""

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)

    return redirect('/')
