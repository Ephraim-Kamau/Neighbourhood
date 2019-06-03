from django import forms
from .models import Businesses,Profile,Posts

class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude = ['userId']

class NewPostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        exclude=['poster_id']

class NewBusinessesForm(forms.ModelForm):
    class Meta:
        model=Businesses
        exclude=[]
        