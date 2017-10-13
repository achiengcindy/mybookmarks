
from django.conf.urls import url
from bookmarksapp import views



urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', views.bookmark_user, name='bookmarksapp.bookmark_user'),
    #url(r'^user/(?P<username>[\w.@+-]+)/$', views.bookmark_user, name='bookmarksapp.bookmark_user'),
    url(r'^$', views.bookmark_list, name='bookmarksapp.bookmark_list'),

]



