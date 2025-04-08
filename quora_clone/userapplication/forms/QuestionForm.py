from django import forms
from ..models.QuestionModel import Question
from ..models.AnswerModel import Answer
from ..models.CommentModel import Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'image']