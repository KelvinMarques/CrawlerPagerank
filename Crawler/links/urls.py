from django.urls import path

from . import views as v
urlpatterns = [
    path('', v.getURL, name="home"),
    path('Crawler', v.crawlerView, name="Crawler")
]