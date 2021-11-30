from django import forms


class AnalysisForm(forms.Form):
    model = forms.ChoiceField('Default model')
    score = forms.FloatField('Confidence score threshold')
    inputs = forms.CharField(label='Input text')
    # submit = forms.Submit('Submit')