from web.views import dashboard
from django.conf.urls import url

urlpatterns = [
    url(
        r'^last-measurements$'
        , dashboard.get_last_measurements
        , name='last-measurements'
    ),
    url(
        r'^last-measurements/(?P<amount>\d+)$'
        , dashboard.get_last_measurements
        , name='last-measurements'
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
