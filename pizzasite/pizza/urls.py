from django.conf.urls import url

from . import views

app_name = "pizza"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^menu/(?P<linkstr>.+)/$', views.detail, name='detail'),
    url(r'^addchoice/(?P<linkstr>.+)/$', views.addchoice, name='addchoice'),
]
