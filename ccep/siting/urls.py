from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /counties/
    url(r'^$', views.index, name='index'),
    # ex: /counties/5/
    url(r'^(?P<county_id>[0-9]+)/$', views.detail, name='detail'),
]
