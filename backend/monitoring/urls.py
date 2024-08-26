from django.urls import path
from .views import ServerStatusListCreate, server_status

urlpatterns = [
    path('api/server-status/', ServerStatusListCreate.as_view(), name='server-status-list-create'),
    path('api/server-status/metrics/', server_status, name='server-status-metrics'),
]
