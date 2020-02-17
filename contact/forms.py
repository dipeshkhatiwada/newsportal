from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'नाम (अनिवार्य)'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'इमेल (अनिवार्य)'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'विषय (अनिवार्य)'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Contact
        # fields = ['title', ]
        # exclude = ['title', ]
        fields = ['name','email','subject','message',]
