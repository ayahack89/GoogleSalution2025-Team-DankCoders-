from django import forms
from .models import documents

class DocumentForm(forms.ModelForm):
    class Meta:
        model = documents
        fields = ['user', 'document_name', 'document']
class AdminLoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username"})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"})
    )