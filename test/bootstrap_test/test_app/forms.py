from django import forms

class TestForm(forms.Form):
  char_field = forms.CharField()
  text_area = forms.CharField(widget=forms.Textarea)