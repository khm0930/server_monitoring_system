from django.db import models

class ServerStatus(models.Model):
    server_name = models.CharField(max_length=255)  # 서버 이름
    cpu_usage = models.FloatField()  # CPU 사용률
    memory_usage = models.FloatField()  # 메모리 사용량
    disk_usage = models.FloatField()  # 디스크 사용량
    network_traffic = models.FloatField()  # 네트워크 트래픽
    timestamp = models.DateTimeField(auto_now_add=True)  # 데이터 수집 시간
def __str__(self):
    return f"CPU: {self.cpu_usage}%, Memory: {self.memory_percentage}%"
