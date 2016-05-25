from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import json
from django.core import serializers
import requests
import bs4

#This is for getting app ratings from Google Play
android_app_id = "jp.co.rakuten.android"
android_app_data_content = requests.get('https://play.google.com/store/apps/details?id='+android_app_id+'&hl=ja')
soup = bs4.BeautifulSoup(android_app_data_content.text, "html.parser")
android_app_rating = soup.find_all('div', attrs={'class': 'score'})
for item in android_app_rating:
    print(item.text)

android_app_review = soup.find_all('div', attrs={'class': 'review-text'})
print(len(android_app_review))
for item in android_app_review:
    print(item.text)

feature_reviews_android = soup.findAll('div', attrs={'class': 'single-review'})

def android_dashboard_index(request):

    return render(request, 'RatingScrape/android_dashboard.html')

def get_android_ratings(request):
    return HttpResponseRedirect(reverse("RatingScrape:android_dashboard_index"))

def delete_all_android_review_entry(request):
    return HttpResponseRedirect(reverse("RatingScrape:android_dashboard_index"))

def get_android_json_test(request):
    review_data = []

    #context['data'] = serializers.serialize('json', str(android_app_review))
    for item in feature_reviews_android:
        single_review_data = {}
        author_name = item.find('span', attrs={'class': 'author-name'})
        single_review_data["author_name"] = author_name.get_text()

        review_title = item.find('span', attrs={'class': 'review-title'})
        single_review_data["review_title"] = review_title.get_text()

        review_body = item.find('div', attrs={'class': 'review-body'})
        single_review_data["review_body"] = review_body.get_text()
        review_data.append(single_review_data)

        star_rating = item.find('div', attrs={'class': 'tiny-star'})['aria-label']
        single_review_data["star_rating_text"] = star_rating

        review_date = item.find('span', attrs={'class': 'review-date'})
        single_review_data["review_date"] = review_date.get_text()

    return HttpResponse(json.dumps(review_data), content_type='application/json')
