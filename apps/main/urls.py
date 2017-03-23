from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^$', views.index),
    url(r'^sessions$', views.login_user),
    url(r'^users$', views.create_user),
    url(r'^view_dashboard$', views.view_dashboard),
]