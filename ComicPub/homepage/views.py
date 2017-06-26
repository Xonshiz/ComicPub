# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ComicPub.settings import WEBSITE_NAME
from django.views import generic
from comics.models import Comic, ComicChapter


def homepage_index(request):
    # return HttpResponse("<h1>Hailo!</h1>")
    return render(request, "index.html", {"WEBSITE_NAME" : WEBSITE_NAME, "comic_information" : Comic.objects.all(), "total_comics" : Comic.objects.all().count(), "chapters_information" : ComicChapter.objects.all()})

# class HomePageIndex(generic.ListView):
#     context_object_name = "comic_list"
#     template_name = "index.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(HomePageIndex, self).get_context_data(**kwargs)
#         context['WEBSITE_NAME'] = WEBSITE_NAME
#
#         return context
#
#     def get_queryset(self):
#         return (Comic.objects.all(), ComicChapter.objects.all())