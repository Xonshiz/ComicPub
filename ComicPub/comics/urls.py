from django.conf.urls import url
from . import views

app_name = "comics"

urlpatterns = [
    # /comics/
    url(r'^$', views.ALLComics.as_view(), name="comic_list"),
    # /comics/comic_id/
    url(r'^(?P<pk>[\d]+)/$', views.ComicDetails.as_view(), name="comic_details"),
    # /comics/comic_id/reader/c1
    url(r'^(?P<pk>[\d]+)/reader/[Cc](?P<chapter_number>[\d]+)/$', views.comic_chapter, name="comic_chapter"),
    # url(r'^(?P<pk>[\d]+)/reader/[Cc](?P<chapter_number>[\d]+)/$', views.comic_chapter, name="comic_chapter"),
]
