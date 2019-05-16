from django.db import models
from datetime import datetime
from officials.models import Official

class Announcement(models.Model):
    official = models.ForeignKey(Official, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now, blank=True)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title