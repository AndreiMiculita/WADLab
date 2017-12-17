from django.conf.urls import url

from . import views
from django.conf.urls import include, url

app_name = "pizza"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^menu/(?P<linkstr>.+)/$', views.detail, name='detail'),
    url(r'^addorder/(?P<linkstr>.+)/$', views.addorder, name='addorder'),
    url(r'^order/$', views.order, name='order'),
    url('^', include('django.contrib.auth.urls')),
]
