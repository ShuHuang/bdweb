from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = False

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
                                      "Example: The cathode of this Li-ion battery system is LiFePO4."}),
        }
        required = ['confidence', 'ques', 'context']

