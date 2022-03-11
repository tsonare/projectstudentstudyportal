from this import d
from rest_framework import serializers
from dashboard.models import Note, Homework, Todo


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["user", "title", "description"]


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ["user", "subject", "title", "description", "status"]


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["user", "title", "todo_status"]
