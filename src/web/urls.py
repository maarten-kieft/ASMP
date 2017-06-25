from web.views import dashboard
from django.conf.urls import url

urlpatterns = [
    url(
        r'^last-current-usage$'
        , dashboard.get_last_current_usage
        , name='last-current-usage'
    ),
    url(
        r'^last-current-usage/(?P<amount>\d+)$'
        , dashboard.get_last_current_usage
        , name='last-current-usage'
    ),
    url(
        r'^statistics$'
        , dashboard.get_statistics
        , name='get_statistics'
    ),
    url(
        r'^graph-overview-data/(?P<period>\w{0,15})/(?P<start_date>\d{4}-\d{2}-\d{2})$'
        , dashboard.get_overview_graph_data
        , name='get_overview_graph_data'
    ),
    url(
        r'^graph-overview-data$'
        , dashboard.get_overview_graph_data
        , name='get_overview_graph_data'
    ),
    url(
        r'^$'
        , dashboard.index
        , name='dashboard'
    ),
]
