from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django import forms

from apps.phonebook_app.models import PhonebookUser


class SignUpForm(UserCreationForm):
    error_messages = {
        'password_mismatch': 'Пароли не совпадают.',
    }
    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput,
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = PhonebookUser
        fields = ('username', 'name', 'surname', 'phone', 'email', 'age', 'gender', 'work_status', 'city',
                  'address', 'password1', 'password2')


class UserForm(forms.ModelForm):
    class Meta:
        model = PhonebookUser
        fields = ('username', 'name', 'surname', 'phone', 'email', 'age', 'gender', 'work_status', 'city', 'address')