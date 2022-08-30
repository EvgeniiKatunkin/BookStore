from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Name", min_length=2, max_length=20)
    age = forms.IntegerField(label="Age", min_value=1, max_value=120)
    email = forms.EmailField(label="Email")
    advert = forms.BooleanField(label="Do you agree to receive advertisement", required=False)
