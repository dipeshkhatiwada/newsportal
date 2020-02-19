from django import forms
from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Name'}))
    link = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Link'}))
    class Meta:
        model = Advertisement
        fields = ['name','link','image','status',]
