from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=260, required=True)

    def saveUser(self):
        user = self.save(commit=False)
        user.first_name = self.cleaned_data['first_name'].title()
        user.last_name = self.cleaned_data['last_name'].title()
        user.email = self.cleaned_data['email']
        user.username = user.email
        user.save()
        return  user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )