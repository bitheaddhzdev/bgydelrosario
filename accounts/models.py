from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=100, blank=True)
    birthplace = models.CharField(max_length=200, blank=True)
    birthdate = models.DateField(default=datetime.now)
    house_num = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    zone = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    religion = models.CharField(max_length=100, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='photos/%Y/%m/%d/', blank=True)
    date_created = models.DateTimeField(default=datetime.now)
    bio = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name   

