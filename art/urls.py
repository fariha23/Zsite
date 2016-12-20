from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail, name = 'detail'),
    url(r'^post_url/$', views.post_art, name = 'post_art'),
]
