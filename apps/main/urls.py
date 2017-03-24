from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^$', views.index),
    url(r'^sessions$', views.login_user),
    url(r'^users$', views.create_user),
    url(r'^view_dashboard$', views.view_dashboard),
    url(r'^logout$', views.logout),
    url(r'^contrib_quote$',views.contrib_quote),
    url(r'^favorites/(?P<id>\d+)/$', views.favorites),
    url(r'^remove/(?P<id>\d+)/$', views.remove),
    url(r'^users/(?P<id>\d+)/$', views.user_info),
]
