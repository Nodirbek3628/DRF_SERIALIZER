from rest_framework import serializers
from django.utils import timezone
from .models import Category,Task

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['id','name','description','category','status','due_date','created_at','user']

        # object leve
    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError({'Due_date': 'Hozirgi vaqtdan keyinni tanlang'})
        
        return value