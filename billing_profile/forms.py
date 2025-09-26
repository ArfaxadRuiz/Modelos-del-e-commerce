from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # username y las contraseñas las va a manejar UserCreationForm
        fields = ("username", "email", "password1", "password2")