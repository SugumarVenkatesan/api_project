from django import forms
from . import config

class APIListForm(forms.Form):
    api_list = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices= [(choice.value, choice.name) for choice in config.APIList])
