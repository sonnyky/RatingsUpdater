__author__ = 'sonny.kurniawan'
from django.conf.urls import url
from . import views

app_name = "RatingScrape"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^android/', views.android_dashboard_index, name='android_dashboard_index'),
    url(r'^ios_app_review_fragment/', views.ios_app_review_fragment, name='ios_app_review_fragment'),
    url(r'^android_app_review_fragment/', views.android_app_review_fragment, name='android_app_review_fragment'),
    url(r'^ios_app_rating_fragment/', views.ios_app_rating_fragment, name='ios_app_rating_fragment'),
    url(r'^android_app_rating_fragment/', views.android_app_rating_fragment, name='android_app_rating_fragment'),
    url(r'^delete_entry/(?P<entry_id>\d+)$', views.delete_entry, name='delete_entry'),
    url(r'^delete_android_rating_entry/(?P<entry_id>\d+)$', views.delete_android_rating_entry, name='delete_android_rating_entry'),
    url(r'^delete_review_entry/(?P<review_id>\d+)$', views.delete_review_entry, name='delete_review_entry'),
    url(r'^delete_android_review_entry/(?P<review_id>\d+)$', views.delete_android_review_entry, name='delete_android_review_entry'),
    url(r'^delete_all_review_entry/', views.delete_all_review_entry, name='delete_all_review_entry'),
    url(r'^delete_all_android_review_entry/', views.delete_all_android_review_entry, name='delete_all_android_review_entry'),
    url(r'^get_ratings/', views.get_ratings, name='get_ratings'),
    url(r'^get_android_ratings/', views.get_android_ratings, name='get_android_ratings'),
    url(r'^get_reviews/', views.get_reviews, name='get_reviews'),
    url(r'^get_android_reviews/', views.get_android_reviews, name='get_android_reviews'),
    url(r'^get_json/', views.get_json, name='get_json'),
    url(r'^filter_by_keyword/', views.filter_by_keyword, name='filter_by_keyword'),
    url(r'^filter_android_review_by_keyword/', views.filter_android_review_by_keyword, name='filter_android_review_by_keyword'),
]
