from .models import Task
from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 50)
    description = serializers.CharField(max_length = 50)
    completed= serializers.BooleanField(default=False)
    

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title",instance.title)
        instance.description = validated_data.get("description",instance.description)
        instance.completed = validated_data.get("completed", instance.completed)
        instance.save()
        return instance    