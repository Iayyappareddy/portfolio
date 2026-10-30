from django import forms
from .models import Message

class Forms(forms.ModelForm):
    class Meta:
        model=Message
        fields=['name','email','message']