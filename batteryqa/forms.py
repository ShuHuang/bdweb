from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['model_name', 'confidence', 'ques', 'context']#, 'answer', 'score']