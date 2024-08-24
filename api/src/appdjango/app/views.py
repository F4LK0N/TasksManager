from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, Work
from .serializers import TaskSerializer, WorkSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
