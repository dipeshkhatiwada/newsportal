from django import forms
from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    link = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Link'}))
    class Meta:
        model = Advertisement
        fields = ['link','image','status',]
