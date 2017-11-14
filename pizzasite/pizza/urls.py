from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^menu/$', views.menu, name='menu'),
    # ex: /polls/5/
    url(r'^menu/(?P<linkstr>.+)/$', views.detail, name='detail'),
]
