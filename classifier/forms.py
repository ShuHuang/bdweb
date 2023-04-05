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
            'text': forms.Textarea(
                attrs={'placeholder': "We have now dereprecated the interactive function, previously deprecated due to the large size of LLMs.\n"
                                        "For large-scale data extraction, please use the Python code of BatteryBERT and BatteryDataExtractor, and run extraction in parallel on an HPC machine for optimal performance.\n"}),
                }
        required = ['text']
