from django import forms


class YearForm(forms.Form):
    year = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter WDC year', 'type': "number", 'id':"year"}
    ))
