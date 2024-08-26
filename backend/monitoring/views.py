from django.shortcuts import render
from rest_framework import generics
from .models import ServerStatus
from .serializers import ServerStatusSerializer
import psutil
from django.http import JsonResponse

class ServerStatusListCreate(generics.ListCreateAPIView):
    queryset = ServerStatus.objects.all()
    serializer_class = ServerStatusSerializer


def server_status(request):
    cpu_usage = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    response_data = {
        'cpu_usage': cpu_usage,
        'memory_total': memory_info.total,
        'memory_used': memory_info.used,
        'memory_percentage': memory_info.percent,
    }
    return JsonResponse(response_data)
# Create your views here.
