from . import views
from django.conf.urls import url

urlpatterns = [
    url(
        r'^last-current-usage$',
        views.get_last_current_usage
        , name='last-current-usage'
    ),
    url(
        r'^statistics$'
        , views.get_statistics
        , name='get_statistics'
    ),
    url(
        r'^graph-overview-data/(?P<period>\w{0,15})/(?P<start_date>\d{4}-\d{2}-\d{2})$',
        views.get_overview_graph_data,
        name='get_overview_graph_data'
    ),
    url(
        r'^graph-overview-data$',
        views.get_overview_graph_data,
        name='get_overview_graph_data'
    ),
    url(
        r'^$',
        views.dashboard,
        name='dashboard'
    ),
]
