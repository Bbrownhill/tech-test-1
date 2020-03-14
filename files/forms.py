from django import forms
from .models import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('created_at', 'owner', 'location',)
        exclude = ('created_at', 'owner', )
