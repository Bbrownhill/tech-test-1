from django.db import models

# Create your models here.
class File(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=75)
    location = models.FileField(upload_to='.')

    def __str__(self):
        return self.file_name
