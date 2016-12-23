from django.db import models
from django.forms.widgets import ClearableFileInput, CheckboxInput
from django.conf import settings
from django.contrib.auth.models import User

class Art(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    img_url = models.ImageField(upload_to ='gallery')
    medium = models.CharField(max_length=50, default='Pencils')
    description = models.CharField(max_length=500, default="Write something about your art!!")

    def __str__(self):
        return self.name
