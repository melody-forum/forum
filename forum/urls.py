"""forum URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from post import views as post_views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'post/list/',post_views.post_list),
    url(r'post/create/',post_views.post_create),
    url(r'post/edit/',post_views.edit_post), #修改
    url(r'post/read/',post_views.read_post),
    url(r'post/search/',post_views.post_search),
]
