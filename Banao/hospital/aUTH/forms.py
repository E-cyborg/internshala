from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import cuser

class LoginForm(forms.Form):
    email_or_username = forms.CharField(
        label="Email or Username",
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "Enter email or username"})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"})
    )


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = cuser
        fields = (
            'username', 'first_name', 'last_name', 'email',
            'password1', 'password2',
            'profile_picture', 'address_line1', 'city', 'state', 'pincode','user_type'
        )
