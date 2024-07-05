from django import forms
from .models import comment


class commentform(forms.ModelForm):
     class Meta:
        model = comment
        fields = (
            "body",

        )
        
        widgets = {
            "body": forms.TextInput(attrs={
                "class": "form-control", "id": "body",
                "placeholder": "Your comment", "required": "required",
                "data-validation-required-message": "Please enter your comment",
                

            }),
        }