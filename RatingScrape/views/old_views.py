from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from urllib.request import urlopen
from ..models import RatingStars
from ..models import UserReviewComments
import json
from django.core import serializers
from RatingScrape.tasks import get_ios_ratings_periodic

# This is for getting app ratings from iTunes
app_id = 419267350
target_url = "https://itunes.apple.com/lookup?id=" + str(app_id) + "&country=jp"
content = urlopen(target_url).read().decode('utf8')
content_data = json.loads(content)

# This is for getting user comments from iTunes
user_comments = urlopen("http://itunes.apple.com/jp/rss/customerreviews/id="+str(app_id)+"/json").read().decode("utf8")
user_comments_data = json.loads(user_comments)

# Create your views here.
def index(request):
    RatingStars.objects.all()
    context = dict()
    context['ratings'] = RatingStars.objects.all()
    return render(request, 'RatingScrape/dashboard.html', context)

def ios_app_review_fragment(request):
    UserReviewComments.objects.all()
    context = dict()
    context['reviews'] = UserReviewComments.objects.all()
    context['length'] = len(UserReviewComments.objects.all())
    return render(request, 'RatingScrape/ios_app_review_fragment.html', context)

def ios_app_rating_fragment(request):
    RatingStars.objects.all()
    context = dict()
    context['ratings'] = RatingStars.objects.all()
    return render(request, 'RatingScrape/ios_app_rating_fragment.html', context)

def get_ratings(request):
    RatingStars.objects.create(
        star_number = content_data['results'][0]['averageUserRatingForCurrentVersion'],
        title = content_data['results'][0]['trackName'],
        text = "Other text",
    )
    context = dict()
    context['ratings'] = RatingStars.objects.all()
    return HttpResponseRedirect(reverse("RatingScrape:index"))

def delete_entry(request, entry_id):
    RatingStars.objects.get(pk=entry_id).delete()
    return HttpResponseRedirect(reverse("RatingScrape:index"))

def delete_review_entry(request, review_id):
    UserReviewComments.objects.get(pk=review_id).delete()
    return HttpResponseRedirect(reverse("RatingScrape:index"))

def delete_all_review_entry(request):
    UserReviewComments.objects.all().delete()
    return HttpResponseRedirect(reverse("RatingScrape:index"))

def add_review_to_table_if_new_and_unique():
    for i in user_comments_data['feed']['entry']:
        if 'author' in i:
            if UserReviewComments.objects.filter(review_id=i['id']['label']):
                pass
            else:
                UserReviewComments.objects.create(
                    author = i['author']['name']['label'],
                    comment = i['content']['label'],
                    review_id = i['id']['label'],
                    rating_given_by_user = i['im:rating']['label'],
                    version_rated = i['im:version']['label']
                )

    return HttpResponse("OK")

def get_reviews(request):
    add_review_to_table_if_new_and_unique()
    context = dict()
    context['reviews'] = serializers.serialize('json', UserReviewComments.objects.all())
    struct = json.loads(context['reviews'])
    return HttpResponse(json.dumps(struct), content_type='application/json')

def go_to_top_page(request):
    return HttpResponseRedirect(reverse("RatingScrape:index"))
