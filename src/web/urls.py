from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^d2$', views.dashboard2, name='dashboard2'),
    url(r'^$', views.dashboard, name='dashboard'),
]
