from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail, name = 'detail'),
    url(r'^post_url/$', views.post_art, name = 'post_art'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += [
    url(r'^media/(?P<path>.*)$',serve, {'document_root': settings.MEDIA_ROOT,}),
    ]
