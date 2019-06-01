from django import forms
from .models import Businesses,Profile,Posts

class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude = []

class NewPostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        exclude=[]

class NewBusinessesForm(forms.ModelForm):
    class Meta:
        model=Businesses
        exclude=[]
        