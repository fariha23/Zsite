from django.forms import ModelForm, Textarea
from django import forms
from .models import Art
from django.utils.translation import ugettext_lazy as _

class ArtForm(ModelForm):
    class Meta:
        model = Art
        fields = ('name', 'img_url', 'medium', 'description' )
        labels = {
        'name':_('Name this Art'),
        'img_url':_('Upload Art'),
        'medium':_('Medium of the Art'),
        'description':_('Description')
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    Password = forms.CharField(widget=forms.PasswordInput())
