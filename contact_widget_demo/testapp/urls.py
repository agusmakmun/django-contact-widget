from django.conf.urls import url
from testapp.views import homepage

urlpatterns = [
    url(r'^$', homepage, name='homepage'),
]
