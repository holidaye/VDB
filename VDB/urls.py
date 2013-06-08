from django.conf.urls.defaults import *
from VDB.view import hello
urlpatterns = patterns('',
('^hello/$', hello),
)