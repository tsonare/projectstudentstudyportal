from rest_framework import serializers
from dashboard.models import Note, Homework, Todo


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Note
        fields = ["id", "user", "title", "description"]


class HomeworkSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Homework
        fields = ["user", "subject", "title", "description", "status"]


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Todo
        fields = ["user", "title", "todo_status"]
