from django.conf.urls import url
from services import views

urlpatterns = [
    url(r'^service/(?P<url_name>\w+)/$', views.cat, name='service'),
    url(r'^service/(?P<url_name>\w+)/(?P<url>\w+)/$', views.service, name='service1')
]