from django.db import models
from django.forms.widgets import ClearableFileInput, CheckboxInput
from django.conf import settings

class Art(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.ImageField(upload_to ='gallery')
    medium = models.CharField(max_length=50, default='Pencils')
    description = models.CharField(max_length=500, default="Coming Soon")

    def __str__(self):
        return self.name
