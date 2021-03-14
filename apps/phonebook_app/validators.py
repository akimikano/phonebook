from gettext import ngettext
from django.core.exceptions import ValidationError


class MyCustomMinimumLengthValidator(object):
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "Пароль должен содержать не менее 8 символов.",
                    "Пароль должен содержать не менее 8 символов.",
                    self.min_length
                ),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return ngettext(
            "Пароль должен содержать не менее 8 символов.",
            "Пароль должен содержать не менее 8 символов.",
            self.min_length
        ) % {'min_length': self.min_length}


