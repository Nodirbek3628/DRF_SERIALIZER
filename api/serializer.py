from rest_framework import serializers
from .models import Category,Task

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'

class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Task
        fields = '__all__'