import datetime
#import itunes ; this is not working until python-itunes supports python 3.x

from urllib.request import urlopen
from django.db import models
from django.utils import timezone

default_text = 'DEFAULT_TEXT'
# Create your models here.
class RatingStars(models.Model):

    title = models.TextField(max_length=255, default="Default")
    text = models.TextField(max_length=255 , default="Default")
    star_number = models.DecimalField(max_digits=2, decimal_places=1, default=9.9)
    time_stamp = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return str(self.title)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def update_field(self, key, value):
        getattr(self, key)
        setattr(self, key, value)