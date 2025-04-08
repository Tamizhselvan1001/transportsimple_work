from django import forms
from ..models.CommentModel import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text','image']