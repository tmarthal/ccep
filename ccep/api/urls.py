from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /geocode/5/
    url(r'^geocode$', views.geocode, name='geocode'),
]
