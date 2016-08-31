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
from django.conf.urls import url
from django.contrib import admin
from views import *
from User import views as user_views

urlpatterns = [
    url(r'^$', landingPage, name='landingPage'),
    url(r'^lesson/(\d+)/$', lessonView, name='lessonView'),
    url(r'^classroom/$', lessonView, name='classroom'),
    url(r'^login/$', user_views.login, name='login'),

    url(r'^admin/', admin.site.urls)
]
