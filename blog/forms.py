from django.forms import ModelForm
from django import forms
from .models import *


class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
    