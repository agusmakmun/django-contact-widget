from django.conf.urls import url
from contact_widget.views import contact_view

urlpatterns = [
    url(r'^contact_widget/$', contact_view, name='contact_widget'),
]
