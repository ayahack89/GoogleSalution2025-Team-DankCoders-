from django import forms
from .models import documents

class DocumentForm(forms.ModelForm):
    class Meta:
        model = documents
        fields = ['user', 'document_name', 'document']
