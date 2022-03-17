from rest_framework import serializers
from dashboard.models import Note, Homework, Todo


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ['username', 'password']


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Note
        fields = ["id", "user", "title", "description"]


class HomeworkSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Homework
        fields = ["id", "user", "subject", "title", "description", "status"]


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Todo
        fields = ["id", "user", "title", "todo_status"]
