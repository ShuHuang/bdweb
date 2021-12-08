from django import forms
from .models import TextClassifier


class TextClassifierForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = TextClassifier
        fields = ['text']
        widgets = {
            'search': forms.TextInput(
                attrs={'placeholder': "Input a paragraph of abstract in here.",
                       "style": "width: 35rem;"}),
        }
        required = ['text']
