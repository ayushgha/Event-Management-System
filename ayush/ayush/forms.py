from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    # CHOICES = [
    #     ('',''),
    #     ('bloodbank' ,'BloodBank'),
    #     ('hospital', 'Hospital'),
    #     ('user', 'User'),
    # ]
    #
    # email = forms.EmailField()
    # who = forms.CharField(label='Who are you?', widget=forms.Select(choices=CHOICES))


    class Meta:
        model= User
        fields = ['username','email','password1','password2']


