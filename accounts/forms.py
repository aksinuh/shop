from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class Registirationform(forms.ModelForm):

    confirim_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Confirim password", "required": "required",
        "style": "margin-bottom: 20px;",
    }))
    
    class Meta:
        model = User
        fields = (
            "username",
            "full_name",
            "email",
            "password",
        )
        
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "username", "required": "required",
                "style": "margin-bottom: 20px;",

            }),            
            
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Full name", "required": "required",
                "style": "margin-bottom: 20px;",

            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email", "required": "required",
                "style": "margin-bottom: 20px;",
                
            }),
            "password": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Password", "required": "required",
                "style": "margin-bottom: 20px;",


            }),
        }
        
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     full_name = self.cleaned_data.get('full_name')
    #     first_name, last_name = full_name.split(' ', 1)
    #     user.first_name = first_name
    #     user.last_name = last_name
    #     user.email = self.cleaned_data.get('email')
    #     if commit:
    #         user.save()
    #     return user
    
    
    def clean(self) -> dict[str, Any]:
        password = self.cleaned_data["password"]
        confirim_password =self.cleaned_data["confirim_password"]
        if password != confirim_password:
            raise forms.ValidationError("Passwords must be same")
        return super().clean()
    

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email",
        "required": "required",
        "style": "margin-bottom: 20px;",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Password",
        "required": "required",
        "style": "margin-bottom: 20px;",
    }))
    
    
