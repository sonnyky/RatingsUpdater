from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from urllib.request import urlopen
from .models import RatingStars
from .models import UserReviewComments
import json
import logging

# This is for getting app ratings from iTunes
app_id = 419267350
content = urlopen("https://itunes.apple.com/lookup?id=" + str(app_id) + "&country=jp").read().decode('utf8')
content_data = json.loads(content)

# This is for getting user comments
user_comments = urlopen("http://itunes.apple.com/jp/rss/customerreviews/id="+str(app_id)+"/json").read().decode("utf8")
user_comments_data = json.loads(user_comments)
#print(user_comments_data['feed']['author']['name']['label'])
#print(user_comments_data['feed']['entry'][1]['author']['name']['label'])
#print(user_comments_data['feed']['entry'][1]['content']['label'])

# Create your views here.
def index(request):
    RatingStars.objects.all()
    UserReviewComments.objects.all()
    #for key, value in content_data.items():
    #   ob.update_field(key, value)
    #   ob.save(update_fields=content_data.keys())

    #objects.all() returns a dictionary so we need to return the appropriate object type
    context = dict()
    context['ratings'] = RatingStars.objects.all()
    context['reviews'] = UserReviewComments.objects.all()
    return render(request, 'RatingScrape/dashboard.html', context)

def get_ratings(request):

    RatingStars.objects.create(
        star_number = content_data['results'][0]['averageUserRating'],
        title = content_data['results'][0]['trackName'],
        text = "Other text",
    )
    context = dict()
    context['ratings'] = RatingStars.objects.all()
    return HttpResponseRedirect(reverse("RatingScrape:index"))

def delete_entry(request, entry_id):
    print("Delete" + entry_id + "++++++++++++++++++++++++++++++++++++++++++++++++++++")
    RatingStars.objects.get(pk=entry_id).delete()
    return HttpResponseRedirect(reverse("RatingScrape:index"))

def delete_review_entry(request, review_id):
    print("Delete review" + review_id + "++++++++++++++++++++++++++++++++++++++++++++++++++++")
    UserReviewComments.objects.get(pk=review_id).delete()
    return HttpResponseRedirect(reverse("RatingScrape:index"))

def delete_all_review_entry(request):
    print("Deleting all reviews from users")
    UserReviewComments.objects.all().delete()
    return HttpResponseRedirect(reverse("RatingScrape:index"))

def get_reviews(request):

    for i in user_comments_data['feed']['entry']:
        if 'author' in i:
            UserReviewComments.objects.create(
                author = i['author']['name']['label'],
                comment = i['content']['label'],
            )
    context = dict()
    context['reviews'] = UserReviewComments.objects.all()
    return HttpResponseRedirect(reverse("RatingScrape:index"))