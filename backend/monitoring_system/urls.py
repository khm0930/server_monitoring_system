
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('monitoring.urls')),  # monitoring 앱의 URL 포함
    path('', include('monitoring.urls')),  # monitoring 앱의 URL 포함
    path('', include('django_prometheus.urls')),  # Prometheus 엔드포인트 추가
]
