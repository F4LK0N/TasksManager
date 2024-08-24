from rest_framework import serializers
from .models import Task, Work

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    subtasks = serializers.SerializerMethodField()
    works = WorkSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def get_subtasks(self, obj):
        return TaskSerializer(obj.subtasks.all(), many=True).data
