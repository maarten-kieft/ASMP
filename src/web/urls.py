from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^last-current-usage$', views.get_last_current_usage, name='last-current-usage'),
    url(r'^statistics$', views.get_statistics, name='get_statistics'),
    url(r'^graph-data$', views.get_graph_data, name='get_graph_data'),
    url(r'^$', views.dashboard, name='dashboard'),
]
