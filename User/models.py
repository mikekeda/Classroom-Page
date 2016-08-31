from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.db import models
from django.forms import ModelForm
from django.conf import settings
import os


class Profile(models.Model):
    """Profile model"""
    user = models.OneToOneField(User)
    picture = models.ImageField(
        upload_to='avatars',
        default=os.path.join(settings.STATIC_URL, 'img/no-avatar.jpg'),
        verbose_name=('picture')
    )
    skype = models.CharField(
        max_length=40,
        default='example',
        verbose_name=_('skype')
    )
    phone_number = models.CharField(
        max_length=15,
        default='+380123456789',
        verbose_name=_('phone number')
    )
    facebook_profile = models.URLField(
        max_length=60,
        default='https://facebook.com/exemple',
        verbose_name=_('facebook profile')
    )

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username


class ProfileForm(ModelForm):
    """ProfileForm model"""
    class Meta:
        model = Profile
        fields = ['picture', 'skype', 'phone_number', 'facebook_profile']


class UserForm(ModelForm):
    """UserForm model"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
