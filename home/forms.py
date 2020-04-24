from django.forms import ModelForm,Textarea
from django import forms
from home.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']

