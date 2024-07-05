from django import forms
from .models import ContactUs


class Contactform(forms.ModelForm):
     class Meta:
        model = ContactUs
        fields = (
            "name",
            "email",
            "subject",
            "message"
        )
        
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control", "id": "name",
                "placeholder": "Your Name", "required": "required",
                "data-validation-required-message": "Please enter your name",
                "style": "margin-bottom: 20px;"

            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control","id": "email",
                "placeholder": "Your email", "required": "required",
                "data-validation-required-message": "Please enter your email",
                "style": "margin-bottom: 20px;"
                
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control", "id": "subject",
                "placeholder": "Your subject", "required": "required",
                "data-validation-required-message": "Please enter a subject",
                "style": "margin-bottom: 20px;"

            }),
            "message": forms.Textarea(attrs={
                "class": "form-control", "id": "message",
                "placeholder": "Your message", "required": "required",
                "data-validation-required-message": "Please enter your message",
                "rows": "6",
                "style": "margin-bottom: 20px;"
            }),
        }