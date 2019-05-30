from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthplace = models.CharField(max_length=200)
    birthdate = models.DateField()
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.userprofile

