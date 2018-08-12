from django.conf.urls import url
from . import views
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='WIFI NETWORK MODEL')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^my-service/api/network/id=(\d+)$', views.fetch_network_by_id),
    url(r'^my-service/api/network/connect', views.connect_device_to_network),
    url(r'^my-service/api/network/report', views.report_network_throughput)
]
# This url can be used without the "?" in the GET api.
#   url(r'^my-service/api/network/id=(\d+)$', views.fetch_network_by_id),
# url(r'^my-service/api/network(?P<id>\w{0,50})/$', views.fetch_network_by_id, name='fetch_network_by_id'),