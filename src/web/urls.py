from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
