from django import forms
from .models import Question, Search


class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Question
        fields = ['select', 'confidence', 'ques', 'context']
        widgets = {
            'ques': forms.TextInput(
                attrs={'placeholder': "Default: What's the device component? (Anode, cathode, electrolyte)",
                       "style": "width: 35rem;"}),
            'confidence': forms.TextInput(
                attrs={'placeholder': "0~1. Default: 0.3",
                       "style": "width: 9;"}),
            'context': forms.Textarea(
                attrs={'placeholder': "Type or paste text in here...\n"
                                      "Default example: The cathode of this Li-ion battery system is LiFePO4."}),
        }
        required = ['confidence', 'ques', 'context']


class SearchForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Search
        fields = ['search']
        widgets = {
            'search': forms.TextInput(
                attrs={'placeholder': "Example: What’s the most common electrolyte in 2019?",
                       "style": "width: 35rem;"}),
        }
        required = ['search']

