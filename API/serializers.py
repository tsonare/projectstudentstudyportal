import imp
from rest_framework import serializers
from dashboard.models import Note, Homework, Todo
from django.contrib.auth.models import User


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Note
        fields = ["id", "user", "title", "description"]

    def create(self, validated_data):
        user = self.context["request"].user
        return self.Meta.model.objects.create(user=user, **validated_data)


class HomeworkSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Homework
        fields = ["id", "user", "subject", "title", "description", "status"]

    def create(self, validated_data):
        # Once you are done, create the instance with the validated data
        user = self.context["request"].user
        return self.Meta.model.objects.create(user=user, **validated_data)


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Todo
        fields = ["id", "user", "title", "todo_status"]

    def create(self, validated_data):
        user = self.context["request"].user
        return self.Meta.model.objects.create(user=user, **validated_data)
