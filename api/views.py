from rest_framework.viewsets import ModelViewSet
from .serializer import CategorySerializer,TaskSerializer
from .models import Category,Task

class CategoryViewSet(ModelViewSet):
    serializer_class=CategorySerializer
    queryset = Category.objects.all()


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()