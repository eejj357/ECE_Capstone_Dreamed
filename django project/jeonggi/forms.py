from django import forms

class YearForm(forms.Form):
    year = forms.IntegerField(min_value=1900, max_value=2023)