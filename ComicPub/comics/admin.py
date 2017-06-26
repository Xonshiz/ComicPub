# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from comics.models import Comic, ComicChapter


# class PageFileInline(admin.TabularInline):
#     model = ComicChapter
#
#
# class PageAdmin(admin.ModelAdmin):
#     inlines = [PageFileInline, ]

# class ChapterInline(admin.TabularInline):
#     model = ComicChapterFiles
#
# class ComicAdmin(admin.ModelAdmin):
#     inlines = [
#         ChapterInline,
#     ]

# admin.site.register(ComicChapter, ComicAdmin)

admin.site.register(Comic)
admin.site.register(ComicChapter)
