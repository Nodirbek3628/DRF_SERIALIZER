from rest_framework import serializers
from django.utils import timezone
from .models import Category,Task


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password2': 'password turi emas'})
        return super().validate(attrs)
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)




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