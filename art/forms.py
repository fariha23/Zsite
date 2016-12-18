from django.forms import ModelForm, Textarea
from .models import Art

class ArtForm(ModelForm):
    class Meta:
        model = Art
        fields = ('name', 'img_url', 'medium', 'description' )
        
