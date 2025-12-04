from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    name = models.CharField(max_length=128,unique=True)
    description = models.TextField(blank=True,null=True)
    status = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,)

    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __repr__(self):
        return self.name


    