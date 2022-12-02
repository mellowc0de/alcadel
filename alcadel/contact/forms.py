from django.forms import ModelForm, TextInput, EmailInput
from django.forms.widgets import Textarea
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('email', 'subject', 'message')
        labels = {
            'email': '',
            'subject': '',
            'message': '',
        }
        widgets = {
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 95%; margin-left: 15px;',
                'placeholder': 'Email'
            }),
            'subject': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 95%; margin-left: 15px;',
                'placeholder': 'Subject'
            }),
            'message': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 95%; margin-left: 15px;',
                'placeholder': 'Message'
            })
        }