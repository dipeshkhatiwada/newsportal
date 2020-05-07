from .models import Category,News,Tag
from django import forms
class NewsCategoryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'title','placeholder':'Category Title'}))
    slug = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'slug','placeholder':'slug'}))
    rank = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Rank'}))

    class Meta:
        model = Category
        fields = '__all__'


class NewsTagForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'title','placeholder':'Tag Title'}))
    slug = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'slug','placeholder':'slug'}))
    rank = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Rank'}))

    class Meta:
        model = Tag
        fields = '__all__'


class NewsForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    slug = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'slug'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset=Category.objects.all())
    class Meta:
        model = News
        fields =['category','tags','title','slug','image','description','status','slider','main_news',]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(attrs={'class': ''}),
        }