from crispy_forms.helper import FormHelper
from django.forms import ModelForm,Textarea
from django.forms import Form
from home.models import Comment
from django import forms

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


class SearchForm(Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Search'}),)



