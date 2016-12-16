from django.db import models
from django.forms.widgets import ClearableFileInput, CheckboxInput

class Art(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.ImageField(upload_to ='images/')
    medium = models.CharField(max_length=50, default='Pencils')
    description = models.TextField(default="Coming Soon")

    def __str__(self):
        return self.name
