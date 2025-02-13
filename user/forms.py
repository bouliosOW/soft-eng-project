from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(label="Username", max_length=15)
    password = forms.CharField(label="Password", max_length=20)


# The form isn't working to create new Account records. Must fix

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=15)
    password = forms.CharField(label="Password", max_length=20)