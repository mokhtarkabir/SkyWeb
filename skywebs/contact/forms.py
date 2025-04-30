from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'project', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border-0 py-3', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border-0 py-3', 'placeholder': 'Your Email'}),
            'project': forms.TextInput(attrs={'class': 'form-control border-0 py-3', 'placeholder': 'Project'}),
            'message': forms.Textarea(attrs={'class': 'w-100 form-control border-0 py-3', 'placeholder': 'Message', 'rows': 6}),
        }