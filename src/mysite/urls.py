"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import login, logout


#urlpatterns = [
   # url(r'^admin/', admin.site.urls),#django 1.9+ does not need to use include()with admin.site.url
   # url(r'^bookmarksapp/',include('bookmarksapp.urls')),

    #LoginView.as_view(template_name='login.html'), name='mysite_login',

   #url(r'^logout/$', 'django.contrib.auth.views.logout',
    #   {'next_page': reverse_lazy('bookmarksapp_bookmark_list')}, name='mysite_logout'),
    
#]


urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^bookmarksapp/',include('bookmarksapp.urls')),

url(r'^login/$', login, {'template_name': 'login.html'},
 name='mysite_login'),
url(r'^logout/$', logout,
{'next_page': reverse_lazy('bookmarksapp_bookmark_list')},    name='mysite_logout'),
]