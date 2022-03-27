from django.db import models
from django.core.files import File

class Song(models.Model):
    # 'id' field is added automatically by django and used as primary key
    uploaded = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='uploads/images/')
    data = models.FileField(upload_to='uploads/')
