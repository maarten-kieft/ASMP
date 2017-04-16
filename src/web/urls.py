from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^last-current-usage$', views.get_last_current_usage, name='last-current-usage'),
    url(r'^$', views.dashboard, name='dashboard'),
]
