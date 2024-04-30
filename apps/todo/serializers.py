from rest_framework import serializers

from apps.todo.models import Todo

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'image', 'is_completed', 'creater_at')