# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from .models import Comic, ComicChapter
from django.http import Http404
from ComicPub.settings import WEBSITE_NAME, DISQUS_URL
from django.shortcuts import render_to_response


app_name = "comics"


class ALLComics(generic.ListView):
    context_object_name = "comic_list"
    template_name = "comic_list.html"

    def get_context_data(self, **kwargs):
        context = super(ALLComics, self).get_context_data(**kwargs)
        context['WEBSITE_NAME'] = WEBSITE_NAME
        context['DISQUS_URL'] = DISQUS_URL

        return context

    def get_queryset(self):
        return Comic.objects.all()


class ComicDetails(generic.DetailView):
    model = Comic
    context_object_name = "comic_details"
    template_name = "comic_details.html"

    def get_context_data(self, **kwargs):
        context = super(ComicDetails, self).get_context_data(**kwargs)
        context['WEBSITE_NAME'] = WEBSITE_NAME
        context['DISQUS_URL'] = DISQUS_URL

        return context

def comic_chapter(request, pk, chapter_number):
    try:
        my_reader = ComicChapter.objects.get(comic=Comic.objects.get(pk=pk), chapter_number=chapter_number)
    except ComicChapter.DoesNotExist:
        raise Http404("<h1> Seems like that chapter has not been released yet!")
    return render(request, "comic_chapter.html",
                  {"chapter_data": my_reader, "WEBSITE_NAME": WEBSITE_NAME, "DISQUS_URL": DISQUS_URL})

def handler404(request):
    response = render_to_response('ErrorPages/404.html', {}, status=404)
    # response.status_code = 404
    return response
