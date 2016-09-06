"""ClassroomPage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.conf import settings
from views import *
from User import views as user_views

urlpatterns = [
    url(r'^$', landing_page, name='landing_page'),
    url(r'^login$', user_views.login, name='login'),
    url(r'^logout$', user_views.logout, name='logout'),
    url('^register$', CreateView.as_view(
        template_name='register.html',
        form_class=UserCreationForm,
        success_url=reverse_lazy('landing_page')
        ), name='register'),

    url(r'^admin/', admin.site.urls),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^markdownx/', include('markdownx.urls')),

    url(r'^classroom/', include('classroom.urls', namespace='classroom'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
