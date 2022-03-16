from django.db import models

class Song(models.Model):
    # 'id' field is added automatically by django and used as primary key
    uploaded = models.DateTimeField(auto_now_add=True)
    data = models.FileField(upload_to='uploads/')
