from django.conf.urls import url
from homepage import views

urlpatterns = [
    url(r'^$', views.homepage_index, name="homepage_index"),
    # url(r'^$', views.HomePageIndex.as_view(), name="homepage_index"),
]
