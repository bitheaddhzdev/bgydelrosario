from django.db import models
from datetime import datetime
class Official(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    is_mvp = models.BooleanField(default=False)
    term_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.first_name + " " + self.last_name
