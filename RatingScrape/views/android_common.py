from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from ..models import AndroidRatingStars
from ..models import AndroidUserReviewComments

import json
from datetime import date

from django.core import serializers
import requests
import bs4

#This is for getting app ratings from Google Play
android_app_id = "jp.co.rakuten.android"
android_app_data_content = requests.get('https://play.google.com/store/apps/details?id='+android_app_id+'&hl=ja')
soup = bs4.BeautifulSoup(android_app_data_content.text, "html.parser")
android_app_rating = soup.find_all('div', attrs={'class': 'score'})
for item in android_app_rating:
    app_rating = item.text

android_app_review = soup.find_all('div', attrs={'class': 'review-text'})

feature_reviews_android = soup.findAll('div', attrs={'class': 'single-review'})

def android_dashboard_index(request):
    AndroidRatingStars.objects.all()
    context = dict()
    context['ratings'] = AndroidRatingStars.objects.all()
    return render(request, 'RatingScrape/android_dashboard.html', context)

def android_app_rating_fragment(request):
    AndroidRatingStars.objects.all()
    context = dict()
    context['ratings'] = AndroidRatingStars.objects.all()
    return render(request, 'RatingScrape/android_app_rating_fragment.html', context)

def android_app_review_fragment(request):
    AndroidUserReviewComments.objects.all()
    context = dict()
    context['reviews'] = AndroidUserReviewComments.objects.all()
    context['length'] = len(AndroidUserReviewComments.objects.all())
    return render(request, 'RatingScrape/android_app_review_fragment.html', context)

def delete_android_review_entry(request, review_id):
    AndroidUserReviewComments.objects.get(pk=review_id).delete()
    return HttpResponseRedirect(reverse("RatingScrape:android_dashboard_index"))

def get_android_ratings(request):

    AndroidRatingStars.objects.create(
        star_number=app_rating,
    )
    context = dict()
    context['ratings'] = AndroidRatingStars.objects.all()
    return HttpResponseRedirect(reverse("RatingScrape:android_dashboard_index"))

def delete_all_android_review_entry(request):
    AndroidUserReviewComments.objects.all().delete()
    return HttpResponseRedirect(reverse("RatingScrape:android_dashboard_index"))

def get_android_reviews_and_remove_duplicates():
    review_data = []
    for item in feature_reviews_android:
        single_review_data = {}
        author_name = item.find('span', attrs={'class': 'author-name'})
        author_name_text = author_name.get_text()
        single_review_data["author_name"] = author_name_text

        review_title = item.find('span', attrs={'class': 'review-title'})
        single_review_data["review_title"] = review_title.get_text()

        review_body = item.find('div', attrs={'class': 'review-body'})
        single_review_data["review_body"] = review_body.get_text()
        review_data.append(single_review_data)

        star_rating = item.find('div', attrs={'class': 'tiny-star'})['aria-label']
        star_rating_text = chunks(star_rating,6,1)
        single_review_data["star_rating_text"] = star_rating_text

        review_timestamp = item.find('span', attrs={'class': 'review-date'})
        review_timestamp_text = review_timestamp.get_text()
        review_date_text = (review_timestamp_text.rsplit('月',1)[1]).rsplit('日',1)[0]
        review_date_month = (review_timestamp_text.rsplit('月',1)[0]).rsplit('年',1)[1]
        review_date_year = review_timestamp_text.rsplit('年',1)[0]
        review_date_object = date(int(review_date_year), int(review_date_month), int(review_date_text))
        single_review_data["review_date"] = review_date_object.strftime('Year %Y Month %m Date %d')

        if AndroidUserReviewComments.objects.filter(author = author_name_text):
            pass
        else:
            AndroidUserReviewComments.objects.create(
                author=author_name.get_text(),
                comment=review_body.get_text(),
                rating_given_by_user=star_rating_text,
            )

    #return HttpResponse(json.dumps(review_data), content_type='application/json')
    return HttpResponse("OK")

def delete_android_rating_entry(request, entry_id):
    AndroidRatingStars.objects.get(pk=entry_id).delete()
    return HttpResponseRedirect(reverse("RatingScrape:android_dashboard_index"))


def get_android_reviews(request):
    get_android_reviews_and_remove_duplicates()
    android_context = dict()
    android_context['android_reviews'] = serializers.serialize('json', AndroidUserReviewComments.objects.all())
    struct = json.loads(android_context['android_reviews'])
    return HttpResponse(json.dumps(struct), content_type='application/json')

def chunks(string, start, end):
    """Produce `n`-character chunks from `s`."""
    return string[start:start+end]

