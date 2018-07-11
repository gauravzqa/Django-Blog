from django.conf.urls import url, include

from . import views

app_name="article"

urlpatterns = [
    url(r'^$', views.article_list,name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]
