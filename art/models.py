from django.db import models

class Art(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)
    medium = models.CharField(max_length=50, default='Pencils')
    description = models.TextField(default="Coming Soon")

    def __str__(self):
        return self.name
