from django.db import models
import os

# Create your models here.
#파일을 업로드하면, File object로 인식된다.
class Photo(models.Model):
    image = models.FileField(null=True, blank=True, upload_to='uploads/')

    def save(self):
        super().save()