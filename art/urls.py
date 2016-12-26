from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail, name = 'detail'),
    url(r'^([0-9]+)/edit/$', views.edit, name = 'edit'),
    url(r'^([0-9]+)/delete/$', views.delete, name = 'delete'),
    url(r'^post_url/$', views.post_art, name = 'post_art'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^like_art/$', views.like_art, name='like_art' )


]

if settings.DEBUG:
    urlpatterns += [
    url(r'^media/(?P<path>.*)$',serve, {'document_root': settings.MEDIA_ROOT,}),
    ]
