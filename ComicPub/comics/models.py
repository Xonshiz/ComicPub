# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ComicPub.settings import WEBSITE_NAME


def comic_upload_location(instance, filename):
    # Learned it from here : https://stackoverflow.com/a/44735394/2408212 (thank the smart people)
    return '{}/{}'.format(str(instance.comic_name).replace(" ", "_").replace(":", " ").replace("/", "").replace("\\", ""), filename)

def comic_banner_upload_location(instance, filename):
    # Learned it from here : https://stackoverflow.com/a/44735394/2408212 (thank the smart people)
    return '{}/{}'.format(str(instance.comic_name).replace(" ", "_").replace(":", " ").replace("/", "").replace("\\", ""), "Banner_" + str(filename))


def comic_chapter_upload_location(instance, filename):
    # Learned it from here : https://stackoverflow.com/a/44735394/2408212 (thank the smart people)
    # /media/Comic_Name/Chapter_Number/
    return '{}/{}/{}'.format(str(instance.chapter.comic.comic_name).replace(" ", "_").replace(":", " ").replace("/", "").replace("\\", ""), instance.chapter.chapter_number, filename)


class Comic(models.Model):
    comic_name = models.CharField(max_length=500, blank=False)
    comic_description = models.TextField(max_length=4000, blank=False)
    comic_author = models.CharField(max_length=250, blank=True)
    comic_artist = models.CharField(max_length=250, blank=True)
    comic_genre = models.CharField(max_length=100, blank=False)
    comic_total_chapters = models.CharField(max_length=100, blank=False, default="Unknown")
    comic_type = models.CharField(max_length=100, blank=False, default="Comic")
    comic_status = models.CharField(max_length=100, default="Ongoing")
    comic_original_name = models.CharField(max_length=100, blank=True, default="None") # For Manga/Manhua/Manhwa
    comic_image = models.FileField(upload_to=comic_upload_location, blank=False, help_text="Please upload a cover with minimum dimensions of 500px X 500px")
    comic_banner_image = models.FileField(upload_to=comic_banner_upload_location, blank=True, help_text="1500px by 500px is recommended. This is an optional field (for now)")
    comic_site_name = WEBSITE_NAME

    def __str__(self):
        return str(self.comic_name) + " ( " + str(self.pk) + ")"


class ComicChapter(models.Model):
    comic = models.ForeignKey(Comic,
                              on_delete=models.CASCADE)  # Let's delete all the chapters related to a particular comic, if comic is deleted. Thanks Bucky!
    chapter_title = models.CharField(max_length=1000, blank=False)
    chapter_number = models.CharField(max_length=1000, blank=False)
    chapter_volume = models.CharField(max_length=1000, blank=True, default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    chapter_images = models.TextField(max_length=20, blank=False, help_text="Just enter the ID of the Imgur Album and not the full URL.")
    # chapter_images = models.FileField(upload_to=comic_chapter_upload_location)

    def __str__(self):
        return str(self.comic.comic_name) + " - " + "V" + str(self.chapter_volume) + " C" + str(self.chapter_number)

# This was code for uploading multiple files in the server. Dropped it for now.
# class ComicChapterFiles(models.Model):
#     chapter = models.ForeignKey(ComicChapter, on_delete=models.CASCADE)
#     # print("Chapter : %s" % chapter.chapter_title)
#     chapter_images = models.FileField(upload_to=comic_chapter_upload_location)
#
#     def __str__(self):
#         print(self.chapter_images.path)
