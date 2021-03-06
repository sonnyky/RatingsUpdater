import datetime
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import jsonfield

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

class AndroidRatingStars(models.Model):

    star_number = models.TextField(max_length=255 , default="Default")
    time_stamp = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return str(self.title)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def update_field(self, key, value):
        getattr(self, key)
        setattr(self, key, value)

class UserReviewComments(models.Model):
    author = models.TextField(max_length= 255, default="DEFAULT")
    comment = models.TextField(max_length= 255, default="DEFAULT")
    review_id = models.TextField(max_length=255, default="DEFAULT")
    rating_given_by_user = models.TextField(max_length=255, default="DEFAULT")
    version_rated = models.TextField(max_length=255, default="DEFAULT")

    def __str__(self):
        return str(self.author)

class AndroidUserReviewComments(models.Model):
    author = models.TextField(max_length=255, default="DEFAULT")
    comment = models.TextField(max_length=255, default="DEFAULT")
    rating_given_by_user = models.TextField(max_length=255, default="DEFAULT")

    def __str__(self):
        return str(self.author)
