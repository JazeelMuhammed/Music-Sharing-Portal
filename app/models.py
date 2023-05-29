from django.db import models
from django.conf import settings

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=20)
    album = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='musics/')
    is_private = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    is_protected = models.BooleanField(default=False)

    def __str__(self):
        self.title
