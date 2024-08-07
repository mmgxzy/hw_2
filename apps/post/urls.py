from django.urls import path
from apps.post.views import about, index, news, contact, time


urlpatterns = [
    path("", index, name='index'),
    path("about/", about, name='about'),
    path("news/", news, name='news'),
    path("con/", contact, name='contact'),
    path("time/", time, name = 'time'),
    
]