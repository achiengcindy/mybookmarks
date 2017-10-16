
from django.conf.urls import url

from bookmarksapp import views



urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', views.bookmark_user, name='bookmarksapp_bookmark_user'),
    #url(r'^user/(?P<username>[\w.@+-]+)/$', views.bookmark_user, name='bookmarksapp.bookmark_user'),
    
    url(r'^create/$',views.bookmark_create,
        name='bookmarksapp_bookmark_create'),
    url(r'^edit/(?P<pk>\d+)/$', views.bookmark_edit,
        name='bookmarksapp_bookmark_edit'),
url(r'^$', views.bookmark_list, name='bookmarksapp_bookmark_list'),

]



