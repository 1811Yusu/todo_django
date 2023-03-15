from rest_framework import serializers

from .models import Todo

class ToDoSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    completed = serializers.BooleanField(required=False)
    created_at = serializers.ReadOnlyField()
    deadline = serializers.DateTimeField()

class UpdateToDoSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    deadline = serializers.DateTimeField(required=False)
    completed = serializers.BooleanField(required=False)

    def update(self, instance: Todo, validated_data: dict):
        print(validated_data)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        # instance.title = validated_data.get('title', instance.title)
        # instance.deadline = validated_data.get('deadline', instance.deadline)
        # instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance
