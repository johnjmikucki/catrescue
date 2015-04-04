from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^about$', views.about),
    url(r'^adoptable$', views.adoptable_list),
    url(r'^$', views.about),
    url(r'^cat/(?P<id>[0-9]+)/$', views.detail),
]
