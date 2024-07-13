from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    contact_number = forms.CharField(label='Contact Number', max_length=15)
    email = forms.EmailField(label='Email', max_length=100)
    gender = forms.ChoiceField(label='Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    education = forms.CharField(label='Education', max_length=200)
    state = forms.CharField(label='State', max_length=30)
