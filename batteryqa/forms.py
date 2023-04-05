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
                attrs={'placeholder': "We have now dereprecated the interactive function, previously deprecated due to the large size of LLMs.\n"
                                      "For large-scale data extraction, please use the Python code of BatteryBERT and BatteryDataExtractor, and run extraction in parallel on an HPC machine for optimal performance.\n"}),
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
            'search': forms.Textarea(
                attrs={'placeholder': "Example: What’s the most common electrolyte in 2019?\n"
                                        "We have now dereprecated the interactive function, previously deprecated due to the large size of LLMs.\n"
                                        "For large-scale data extraction, please use the Python code of BatteryBERT and BatteryDataExtractor, and run extraction in parallel on an HPC machine for optimal performance.\n"}),
                }
        required = ['search']

