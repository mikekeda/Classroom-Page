from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm


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
