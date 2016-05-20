from django.http import HttpResponseRedirect, HttpResponse
from ..models import UserReviewComments
import json

def get_json(request):

    return HttpResponse(json.dumps({'username':"TEST"}), content_type='application/json')