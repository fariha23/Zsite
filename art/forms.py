from django import forms

class ArtForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    img_url = forms.CharField(label='Image URL', max_length=100)
    medium = forms.CharField(label='Medium', max_length=50)
    description = forms.CharField(label='Description')
