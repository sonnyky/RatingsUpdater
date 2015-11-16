from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from urllib.request import urlopen
from .models import RatingStars
import json

app_id = 419267350
content = urlopen("https://itunes.apple.com/lookup?id=" + str(app_id) + "&country=jp").read().decode('utf8')
content_data = json.loads(content)


# Create your views here.
def index(request):
    RatingStars.objects.all()
    #ob = RatingStars.objects.get(id=1)

    #for key, value in content_data.items():
    #   ob.update_field(key, value)
    #   ob.save(update_fields=content_data.keys())

    #ob.update_field("star_number", content_data['results'][0]['averageUserRatingForCurrentVersion'])
    #ob.save(update_fields = ["star_number"])

    #objects.all() returns a dictionary so we need to return the appropriate object type
    context = dict()
    context['ratings'] = RatingStars.objects.all()
    return render(request, 'RatingScrape/dashboard.html', context)

def get_ratings(request):

    RatingStars.objects.create(
        star_number = content_data['results'][0]['averageUserRating'],
        title = content_data['results'][0]['trackName'],
        text = "Other text",
    )
    context = dict()
    context['ratings'] = RatingStars.objects.all()
    return render(request, 'RatingScrape/dashboard.html', context)

def delete_entry(request, entry_id):
    print("Delete" + entry_id + "++++++++++++++++++++++++++++++++++++++++++++++++++++")
    RatingStars.objects.get(pk=entry_id).delete()
    return HttpResponseRedirect(reverse("RatingScrape:index"))