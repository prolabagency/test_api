from rest_framework import serializers
from .models import Category, Todo


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['isActive',]


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'isActive', 'isCompleted']

