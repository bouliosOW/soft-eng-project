from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(label="Username", max_length=10)
    password = forms.CharField(label="Password", max_length=20)