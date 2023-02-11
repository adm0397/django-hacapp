from django import forms


# Create your forms here.
class InstagramForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)


class FacebookForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
