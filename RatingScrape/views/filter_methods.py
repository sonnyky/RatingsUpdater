from django.shortcuts import render
from django.db.models import Q
from urllib.parse import unquote
from django.http import HttpResponseRedirect, HttpResponse
from ..models import UserReviewComments
from ..models import AndroidUserReviewComments

from django.core import serializers
from django.utils.encoding import smart_str, force_text
import json


def get_json(request):

    return HttpResponse(json.dumps({'username':"TEST"}), content_type='application/json')

def filter_by_keyword(request):
    filter_string = request.POST.get('filter_to_use')
    context = dict()
    context['reviews'] = UserReviewComments.objects.filter(comment__icontains=unquote(filter_string,'utf-8'))
    context['length'] = len(context['reviews'])
    return render(request, 'RatingScrape/ios_app_review_fragment.html', context)

def filter_android_review_by_keyword(request):
    filter_string = request.POST.get('filter_to_use')
    context = dict()
    context['reviews'] = AndroidUserReviewComments.objects.filter(comment__icontains=unquote(filter_string,'utf-8'))
    context['length'] = len(context['reviews'])
    return render(request, 'RatingScrape/android_app_review_fragment.html', context)
