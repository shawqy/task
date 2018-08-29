from django import forms
from .models import Snippet

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    phone = forms.CharField()
    age = forms.CharField()
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])
    comment = forms.CharField(widget=forms.Textarea)
    
class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name', 'email', 'phone', 'age', 'gender', 'comment')