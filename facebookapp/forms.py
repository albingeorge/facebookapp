from django import forms

class FacebookForm(forms.Form):
	"""docstring for FacebookForm"""
	url = forms.CharField(max_length=200)