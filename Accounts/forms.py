from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

    def clean_username(self):
        username = self.cleaned_data['username']
        prohibited_words = ['shit', 'fuck', 'bobo']

        username_lower = username.lower()

        for word in prohibited_words:
            if word in username_lower:
                raise ValidationError(
                    f"Username cannot contain the word '{word}'."
                )
        return username