from django import forms
from ..models.AnswerModel import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body','image']