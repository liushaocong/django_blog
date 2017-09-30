from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.index,name='index'),
    # url(r'^edit/$',views.edit_page,name='edit_page'),
    url(r'^edit_body$',views.edit_body,name='edit_body'),
    url(r'^edit/(?P<article_id>[0-9]+)$',views.edit_page,name='edit_page'),
    url(r'^(?P<article_id>[0-9]+)/$',views.details,name='details'),
    url(r'^daomubiji/$',views.daomubiji,name='daomubiji'),
    url(r'^daomubiji/(?P<id>[0-9]+)$',views.daomubiji_page,name='daomubiji_page')
]
