from django.db import models

from datetime import datetime

# Create your models here.
class ShortUrls(models.Model):
    id = models.IntegerField(primary_key=True)
    original_url = models.CharField(max_length=500)
    short_id = models.CharField(max_length=20)
    created_at = models.DateTimeField()