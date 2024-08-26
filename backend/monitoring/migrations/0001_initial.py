# Generated by Django 3.2 on 2024-08-26 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(max_length=255)),
                ('cpu_usage', models.FloatField()),
                ('memory_usage', models.FloatField()),
                ('disk_usage', models.FloatField()),
                ('network_traffic', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
