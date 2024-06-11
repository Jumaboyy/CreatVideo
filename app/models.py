from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

def file_size(value):
    limit = 100 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Fayl juda katta. Hajmi 100 MB dan oshmasligi kerak.')

class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(
        upload_to='lesson/videos/',
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4', 'WMV']),
            file_size
        ]
    )
    description = models.TextField(max_length=1000)