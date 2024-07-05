from django.core.exceptions import ValidationError

def validate_gmail(value):
    if not value.endswith("@gmail.com"):
        raise ValidationError("Email must be gmail!")
    return True